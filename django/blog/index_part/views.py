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
    ten = index_article.objects.all()[:10]
    list=[]
    for i in ten:
        dict = {
            'title' : i.title,
            'type' : i.type,
            'id':i.id,
        }
        list.append(dict)

    return render(request,'html/index_html.html',{'ten':list})


def article_html(request,article_type,article_id):
    for plate in (index_article,
                  automatic_article
                  ,database_article,
                  docker_article,
                  kvm_article,
                  linux_article,
                  vmware_article):

        if  int(article_type) == int(plate.objects.first().type):
            article = plate.objects.get(id = article_id)

    return render(request,'html/article.html',{'article_title':article.title,
                                               'article_time':article.time,
                                               'article_text':article.text})



