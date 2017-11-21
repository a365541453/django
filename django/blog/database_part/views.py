from django.shortcuts import render

# Create your views here.

from database_part.models import database_article

def database_html(request):
    ten = database_article.objects.order_by('-id')[:10]
    list = []
    for i in ten:
        dict = {
            'title': i.title,
            'type': i.type,
            'id': i.id,
        }
        list.append(dict)
    return render(request,'html/database_part.html', {'ten': list})