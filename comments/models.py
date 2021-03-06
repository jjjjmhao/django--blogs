from django.db import models


# Create your models here.

class Comment(models.Model):
    # 信息字段
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    # 评论内容
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    #对应的文章
    #blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
