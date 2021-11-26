from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank = True,null = True)
    post_date = models.DateField(auto_now_add=True)

    def __str___ (self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.id)))

# Create your models here.
