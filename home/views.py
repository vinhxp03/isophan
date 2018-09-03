from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'pages/home.html')
def introduce(request):
	return render(request, 'pages/introduce.html')
def error(request):
	return render(request, 'pages/error.html')
