from django.db import models

# Create your models here.
class vmware_article(models.Model):
	title = models.CharField(max_length=32)
	type = models.CharField(default=None, max_length=10, null=False)
	time = models.DateField()
	text = models.TextField()


	def __str__(self):
		return self.title