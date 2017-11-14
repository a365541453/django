from django.shortcuts import render

# Create your views here.
def database_html(request):
    return render(request,'html/database_part.html')