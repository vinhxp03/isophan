from django.db import models
from tinymce import HTMLField

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = HTMLField('body')
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default=True, blank=True)

	#overide print title shell
	def __str__(self):
		return self.title

	#set letter show short
	def snippet(self):
		return self.body[:100] + "..."

	# #define save set slug for title
	# def save(self, *args, **kwargs):
	# 	self.slug = slugify(self.title, allow_unicode=True)
	# 	super(News, self).save(*args, **kwargs)