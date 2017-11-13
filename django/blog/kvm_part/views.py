from django.shortcuts import render

# Create your views here.
def kvm_html(request):
    return render(request,'html/kvm_part.html')