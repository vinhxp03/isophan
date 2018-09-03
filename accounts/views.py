from django.shortcuts import render, redirect
from home.forms import RegisterForm, LoginForm #override form
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			#login the user
			auth_login(request, user)
			return redirect('/')
	else:
		form = RegisterForm()
	return render(request, 'accounts/register.html', {'form':form})

def login(request):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			#login the user
			user = form.get_user()
			auth_login(request, user)
			return redirect('/')
	else:
		form = LoginForm()
	return render(request, 'accounts/login.html', {'form':form})

def logout(request):
	auth_logout(request)
	return redirect('/')