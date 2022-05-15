from django.db import models

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)

    def __str__(self) :
        return self.content