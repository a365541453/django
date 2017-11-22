from django.db import models

# Create your models here.


class hehuan_image(models.Model):
	title = models.CharField(max_length=32)
	image = models.ImageField()

	def __str__(self):
		return self.title