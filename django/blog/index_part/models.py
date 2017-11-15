from django.db import models
from django import forms


# Create your models here.
class index_article(models.Model):
	title = models.CharField(max_length=32)
	type = models.CharField(default=None, max_length=10, null=False)
	time = models.DateField()
	text = models.TextField()


	def __str__(self):
		return self.title

