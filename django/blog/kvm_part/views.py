from django.shortcuts import render

# Create your views here.

from kvm_part.models import kvm_article

def kvm_html(request):
    ten = kvm_article.objects.order_by('-id')[:10]
    list = []
    for i in ten:
        dict = {
            'title': i.title,
            'type': i.type,
            'id': i.id,
        }
        list.append(dict)
    return render(request,'html/kvm_part.html', {'ten': list})