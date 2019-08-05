from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=120)
    post_publish_date = models.DateTimeField('date published')
    post_content = models.TextField(max_length=500)
    post_author = models.CharField(max_length=24)
    def __str__(self):
        return self.post_title

# class User(models.Model):
#     username = models.CharField(max_length=24)
#     email = models.EmailField()