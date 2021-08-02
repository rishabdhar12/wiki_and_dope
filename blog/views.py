from django.shortcuts import render
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

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


def UserSpecific(request):
	logged_in_user = request.user
	logged_in_user_posts = Post.objects.filter(author=logged_in_user)
	return render(request, 'blog/specific_posts.html', {'posts': logged_in_user_posts})


class PostCreate(LoginRequiredMixin, CreateView):
	model = Post
	fields = ["title", "content", "image"]
	context_object_name = 'create_post'
	template_name = 'blog/create_post.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.author =  self.request.user
		return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ["title", "content", "image"]
	context_object_name = 'update_post'
	template_name = 'blog/update_post.html'
	success_url = reverse_lazy('post')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False