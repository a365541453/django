from django.shortcuts import render

# Create your views here.
from index_part.models import index_article as index

def index_html(request):
    n = index.objects.all()

    return render(request,'html/index_html.html',{'n':n})
