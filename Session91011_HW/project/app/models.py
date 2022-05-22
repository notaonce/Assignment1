from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    author = models.ForeignKey(User, models.CASCADE, related_name='comments')

    def __str__(self) :
        return self.content