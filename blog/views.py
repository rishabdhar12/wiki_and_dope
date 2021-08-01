from django.shortcuts import render
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

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


class PostCreate(LoginRequiredMixin, CreateView):
	model = Post
	fields = ["title", "content", "image"]
	context_object_name = 'create_post'
	template_name = 'blog/create_post.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.author =  self.request.user
		return super(PostCreate, self).form_valid(form)