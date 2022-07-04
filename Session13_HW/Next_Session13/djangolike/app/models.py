from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')

class Like(models.Model) :
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes"
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes"
    )

class Scrap(models.Model) :
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="scraps"
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="scraps"
    )