from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=200, verbose_name='제목 없음')
    detail = models.TextField(verbose_name='내용 없음')
    date = models.DateTimeField(default=timezone.now)
    d_day = models.DateField(default=timezone.now)
        
    def __str__(self):
        return self.title