from django.shortcuts import render

# Create your views here.

from automatic_part.models import automatic_article


def automatic_html(request):
    ten = automatic_article.objects.order_by('-id')[:10]
    list = []
    for i in ten:
        dict = {
            'title': i.title,
            'type': i.type,
            'id': i.id,
        }
        list.append(dict)

    return render(request,'html/automatic_part.html', {'ten': list})
