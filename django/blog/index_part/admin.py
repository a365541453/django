from django.contrib import admin

from django import forms
from django.forms import widgets, models, fields

# Register your models here.
from index_part.models import article


class FlatPageForm(forms.ModelForm):
	class Meta:
		model = article
		exclude = []
		widgets = {
			"type": fields.Select(choices=[
				(1,"one"),
				(2,"two")
			])
		}


@admin.register(article)
class FlatPageAdmin(admin.ModelAdmin):
	form = FlatPageForm
