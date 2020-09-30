from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AnswerForm
from .models import Question, Answer, User
from django.db.models import Count
import datetime

# def home(request):
#     return render(request, 'main_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main_app/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'main_app/profile.html', context)

class QuestionListView(ListView):
    model = Question
    template_name = 'main_app/home.html'
    context_object_name = 'questions'
    ordering = ['-date_posted']
    paginate_by = 5

    def post(self, request):
        # def get_context_data(self, **kwargs):          
        #     context = super(QuestionListView, self).get_context_data(**kwargs) 
        context = {} 
        keyword = request.POST.get("search")                   
        context["questions"] = Question.objects.filter(question__contains = keyword)
        
        # return redirect('home')
        return render(request, 'main_app/home.html', context)
        

class QuestionCreateView(LoginRequiredMixin,CreateView):
    model = Question
    fields = ['title', 'question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionDetailView(DetailView):

    model = Question

    def post(self, request, pk, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.instance.answered_to = Question.objects.get(id=pk)
            form.save()
            messages.success(request, f'Your answer has been posted!')
            return redirect('question-detail', pk)

    def get_context_data(self, *args, **kwargs): 
        context = super(QuestionDetailView, 
             self).get_context_data(*args, **kwargs) 
        # add extra fields here  
        context["form"] = AnswerForm()
        context["answers"] = Answer.objects.filter(answered_to=context["question"])
        context["count"] =  Answer.objects.filter(answered_to=context["question"]).count()
        return context 
    
   

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            False

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            False

class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False

class AnswerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Answer
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            False

class UserListView(ListView):
    model = Question
    template_name = 'main_app/user_profile.html'
    context_object_name = 'questions'
    paginate_by = 5

    def get_queryset(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username','first_name'))
        return Question.objects.filter(author=user).order_by('-date_posted')


