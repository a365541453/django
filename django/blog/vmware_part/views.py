from django.shortcuts import render

# Create your views here.
from vmware_part.models import vmware_article

def vmware_index(request):
	ten = vmware_article.objects.order_by('-id')[:10]
	list = []
	for i in ten:
		dict = {
			'title': i.title,
			'type': i.type,
			'id': i.id,
		}
		list.append(dict)
	return render(request,'html/vmware_part.html', {'ten': list})