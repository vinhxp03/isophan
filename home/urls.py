from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('introduce/', views.introduce, name='introduce'),
	path('error/', views.error, name='error'),
]