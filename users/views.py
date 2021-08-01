from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from .forms import UserRegistrationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

# def CustomRegister(request):
# 	# context_object_name = 'register'
# 	# template_name = 'users/register.html'
# 	if request.method == "POST":
# 		form = UserRegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get("username")
# 			return redirect('home')
# 	else:
# 		form = UserRegistrationForm()
# 	return render(request, 'users/register.html', {'form':form})

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