from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    # APIs for post comment
    path('postComment', views.postComment, name="postComment"),
    path('', views.bloghome, name='bloghome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]