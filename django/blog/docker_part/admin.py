from django.contrib import admin
from docker_part.models import docker_article
# Register your models here.
from django import forms
from django.forms import  fields

# Register your models here.

#form是用来控制显示的，这段代码是用来修改form的默认显示
class FlatPageForm(forms.ModelForm):
	class Meta:
		model = docker_article
		exclude = []
		widgets = {
			"type": fields.Select(choices=[
				(1,"主页"),
				(2,"vmware"),
				(3,"自动化"),
				(4,"KVM"),
				(5,"LInux"),
				(6,"Docker"),
				(7,"数据库"),
			])
		}



#FlatPageForm是form类，不能用来与article一起注册
#所以要将修改好的form类和admin类关联起来
class FlatPageAdmin(admin.ModelAdmin):
	form = FlatPageForm


#再将修改后的admin类的方式来注册article
#article要用admin类的方法来注册
admin.site.register(docker_article, FlatPageAdmin)