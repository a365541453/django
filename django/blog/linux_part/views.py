from django.shortcuts import render

# Create your views here.
from linux_part.models import linux_article

def linux_html(request):
    ten = linux_article.objects.order_by('-id')[:10]
    list = []
    for i in ten:
        dict = {
            'title': i.title,
            'type': i.type,
            'id': i.id,
        }
        list.append(dict)
    return render(request,'html/linux_part.html', {'ten': list})