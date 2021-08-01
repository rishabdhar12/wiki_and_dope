from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

# Create your views here.

def CustomRegister(request):
	# context_object_name = 'register'
	# template_name = 'users/register.html'
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			return redirect('home')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form':form})