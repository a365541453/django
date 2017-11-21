from django.shortcuts import render

# Create your views here.

from docker_part.models import docker_article

def docker_html(request):
    ten = docker_article.objects.order_by('-id')[:10]
    list = []
    for i in ten:
        dict = {
            'title': i.title,
            'type': i.type,
            'id': i.id,
        }
        list.append(dict)
    return render(request,'html/docker_part.html', {'ten': list})