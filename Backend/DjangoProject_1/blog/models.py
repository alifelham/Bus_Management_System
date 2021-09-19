from django.db import models
from django.utils import timezone

#one to many relationship between user and posts since one user will be able to have many posts but a post can have only auth
from django.contrib.auth.models import User 


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    #if a user is deleted them all his posts are also deleted 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #defining what the py shell shows when requested to see the posts 
    def __str__(self):
        return self.title

# class RegisteredForms(models.Model):
#     full_name = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     phone_no = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)