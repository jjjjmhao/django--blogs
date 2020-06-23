from django.contrib import admin
from blog.models import Blog


# Register your models here.
class BlogsAdmin(admin.ModelAdmin):
    list = ['title', 'body', 'excerpt','timestamp']

admin.site.register(Blog, BlogsAdmin)
