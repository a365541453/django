from django.shortcuts import render

# Create your views here.
def oracle_html(request):
    return render(request,'html/oracle_part.html')