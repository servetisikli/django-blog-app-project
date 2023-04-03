from django.contrib import admin
from .models import Category, Post, Like, PostView, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(PostView)
admin.site.register(Comment)
