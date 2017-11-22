from django.shortcuts import render

# Create your views here.
from hehuan.models import hehuan_image

def image(request):
	img = hehuan_image.objects.all()

	return render(request,'image.html')