from django.shortcuts import render

# Create your views here.


def vmware_part(request):
	return render(request,'html/vmware_part.html')