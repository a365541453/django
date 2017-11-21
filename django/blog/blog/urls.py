"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from index_part import views as index_views
from vmware_part import views as vmware_views
from blog import settings
from django.views.generic.base import RedirectView
from automatic_part import views as automatic_views
from docker_part import views as docker_views
from kvm_part import views as kvm_views
from linux_part import views as linux_views
from database_part import views as oracle_views
from django.views import static
##############
from index_part.uploads import upload_image
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_views.index_html),
    url(r'^vmware_part$',vmware_views.vmware_index),
    url(r'^automatic_part$',automatic_views.automatic_html),
    url(r'^docker_part$',docker_views.docker_html),
    url(r'^kvm_part$',kvm_views.kvm_html),
    url(r'^linux_part$',linux_views.linux_html),
    url(r'^database_part$',oracle_views.database_html),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    ###################
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^static/upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^article/(?P<article_type>.*)/(?P<article_id>.*)',index_views.article_html),
    url(r'^article_list/(?P<article_type>.*)',index_views.artcle_list),

]


