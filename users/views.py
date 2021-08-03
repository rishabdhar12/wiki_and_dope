from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from .forms import UserRegistrationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from PIL import Image

from blog.models import Post
from .models import Profile

from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.

class CustomRegister(CreateView):
    form_class = UserRegistrationForm
    context_object_name = "register"
    template_name = 'users/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
    	user = form.save()
    	if user is not None:
    		login(self.request, user)
    	return super(CustomRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
    	if self.request.user.is_authenticated:
    		return redirect("home")
    	return super(CustomRegister, self).get(*args, **kwargs)



class CustomLogin(LoginView):
	fields = "__all__"
	context_object_name = "login"
	template_name = "users/login.html"
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy("home")


def Profile(request):
    return render(request, 'users/profile.html')


@login_required
def UpdateProfile(request):
    model = Profile
    fields = "__all__"
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
        u_form = UserUpdateForm(instance=request.user.profile)

    context={'p_form': p_form, 'u_form': u_form}
    return render(request, 'users/update_profile.html',context)