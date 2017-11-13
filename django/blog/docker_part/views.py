from django.shortcuts import render

# Create your views here.
def docker_html(request):
    return render(request,'html/docker_part.html')