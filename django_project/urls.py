"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app import views as main_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from main_app.views import (QuestionCreateView, 
                            QuestionDetailView, 
                            QuestionListView, 
                            QuestionDeleteView,
                            UserListView,
                            AnswerDeleteView,
                            AnswerUpdateView,
                            QuestionUpdateView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', QuestionListView.as_view(), name='home'),
    path('profile/', main_views.profile, name='profile'),
    path('user/<str:username>/', UserListView.as_view(), name='user-profile'),
    path('register/', main_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main_app/logout.html'), name='logout'),
    path('question/new/', QuestionCreateView.as_view(), name='question-create'), 
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'), 
    path('question/<int:pk>/upvote', main_views.UpvoteQuestion, name='question-upvote'),
    path('question/<int:pk>/downvote', main_views.DownvoteQuestion, name='question-downvote'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'), 
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'), 
    path('answer/<int:pk>/update/', AnswerUpdateView.as_view(), name='answer-update'), 
    path('answer/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer-delete'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)