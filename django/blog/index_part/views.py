# coding=utf-8
from django.shortcuts import render

# Create your views here.
from index_part.models import index_article
from automatic_part.models import automatic_article
from database_part.models import database_article
from docker_part.models import docker_article
from kvm_part.models import kvm_article
from linux_part.models import linux_article
from vmware_part.models import vmware_article


def index_html(request):
	ten = index_article.objects.order_by('-id')[:10]
	list = []
	for i in ten:
		dict = {
			'title': i.title,
			'type': i.type,
			'id': i.id,
		}
		list.append(dict)

	return render(request, 'html/index_html.html', {'ten': list})


def article_html(request, article_type, article_id):
	for plate in (index_article,
	              automatic_article,
	              database_article,
	              docker_article,
	              kvm_article,
	              linux_article,
	              vmware_article):
		if int(article_type) == int(plate.objects.first().type):
			article = plate.objects.get(id=article_id)
	return render(request, 'html/article.html', {'article_title': article.title,
	                                             'article_time': article.time,
	                                             'article_text': article.text})


def artcle_list(request,article_type):
	if int(article_type) == 1:
		article = {'a': 1}
	elif int(article_type) == 2:
		article = {'b': 2}
	elif int(article_type) == 3:
		article = {'c': 3}
	elif int(article_type) == 4:
		article = {'d': 4}
	elif int(article_type) == 5:
		article = {'e': 5}
	elif int(article_type) == 6:
		article = {'f': 6}
	elif int(article_type) == 7:
		article = {'g': 7}

	for plate in (index_article,
	              automatic_article,
	              database_article,
	              docker_article,
	              kvm_article,
	              linux_article,
	              vmware_article):

		if int(article_type) == int(plate.objects.first().type):
			ten = plate.objects.order_by('-id')


	return render(request,'html/article_list.html',{'article':article,'ten':ten})