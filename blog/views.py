from django.shortcuts import render
# from django.http import HttpResponse

from django.views.generic.list import ListView

from .models import Post

# Create your views here.

class Home(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/posts.html'