from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'date']
	list_filter = ['date']
	search_fields = ['title']

admin.site.register(Article, ArticleAdmin)