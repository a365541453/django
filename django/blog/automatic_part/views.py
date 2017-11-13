from django.shortcuts import render

# Create your views here.


def automatic_html(request):
    return render(request,'html/automatic_part.html')
