from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#generic view
from django.views.generic import ListView, DetailView

# Create your views here.
# def list(request):
# 	articles = Article.objects.all().order_by('date')
# 	return render(request, 'articles/articles.html', {'articles': articles})
class ArticleListView(ListView):
	queryset = Article.objects.all().order_by('date')
	template_name = 'articles/articles.html'
	context_object_name = 'articles'

def details(request, slug):
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_details.html', {'article': article})

	