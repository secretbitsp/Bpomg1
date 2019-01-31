from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.homepage, name="fooldal"),
    url(r'^kapcsolat/$',views.contact, name='kapcsolat'),
    url(r'^szerviz/$',views.szerviz, name="szerviz"),
    url(r'^ujautok/', include('bpcore.urls'))


]
