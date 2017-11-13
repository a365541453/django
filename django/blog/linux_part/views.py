from django.shortcuts import render

# Create your views here.
def linux_html(request):
    return render(request,'html/linux_part.html')