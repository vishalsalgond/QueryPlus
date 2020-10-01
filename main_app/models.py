from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
timezone.localtime(timezone.now())
from django.urls import reverse
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, ** kwargs):
        super().save(*args, ** kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Question(models.Model):
    title = models.CharField(max_length=100, null=True)
    question = RichTextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.ManyToManyField(User, related_name='upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvotes', blank=True)

    # def __str__(self):
    #     return self.question

    def get_absolute_url(self):
        return reverse('home')

class Answer(models.Model):
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answered_to = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content} {self.answered_to}'

    def get_absolute_url(self):
        return reverse('home')
        # return reverse('question-detail', kwargs={'pk': Question.objects.get(id = self.pk).values('id') })