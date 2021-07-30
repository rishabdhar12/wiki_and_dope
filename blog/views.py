from django.shortcuts import render
from django.urls import reverse_lazy
# from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Post

# Create your views here.

class Home(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/posts.html'


class PostDetail(DetailView):
	model = Post
	context_object_name = "post"
	template_name = 'blog/post.html'


class PostCreate(CreateView):
	model = Post
	fields = "__all__"
	context_object_name = 'create_post'
	template_name = 'blog/create_post.html'
	success_url = reverse_lazy('home')