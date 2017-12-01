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
	#取每个部分的前十篇文章，所有部分最新的文章一定在每个部分的文章其中
	automatic_ten = automatic_article.objects.order_by('-id')[:10]
	database_ten = database_article.objects.order_by('-id')[:10]
	docker_ten = docker_article.objects.order_by('-id')[:10]
	kvm_ten = kvm_article.objects.order_by('-id')[:10]
	linux_ten = linux_article.objects.order_by('-id')[:10]
	vmware_ten = vmware_article.objects.order_by('-id')[:10]

	artcle_all = []
	for part_ten in (automatic_ten,database_ten,docker_ten,kvm_ten,linux_ten,vmware_ten):
		for artcle in part_ten:
			artcle_all.append(artcle)

	#冒泡
	for i in range(len(artcle_all)):
		for j in range(i):
			if artcle_all[j].time > artcle_all[j+1].time:
				artcle_all[j],artcle_all[j+1] = artcle_all[j+1],artcle_all[j]

	ten = artcle_all[::-1][0:9]

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
		print(article_type)
		print(plate.objects.first())
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