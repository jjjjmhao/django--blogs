from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    #标题
    title = models.CharField(max_length=150)
    #内容
    body = models.TextField()
    #时间
    timestamp = models.DateTimeField()
    #摘要
    excerpt = models.CharField(max_length=200, blank=True)
# class Category(models.Model):
#     name = models.CharField(max_length=150)
#
# class Tag(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     create_time = models.DateTimeField()
#     modified_time = models.DateTimeField()
#     # 摘要
#     excerpt = models.CharField(max_length=200, blank=True)
#     author = models.ForeignKey(User,on_delete=models.CASCADE)