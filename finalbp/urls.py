from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.homepage, name="fooldal"),
    #url(r'^kapcsolat/$',views.contact, name='kapcsolat'),
    url(r'^szerviz/$',views.szerviz, name="szerviz"),
    url(r'^ujautok/', include('bpcore.urls')),
    url(r'^hasznaltauto/$',views.hello2, name="hasznalt"),
    url(r'^kapcsolat/', include('sendemail.urls')),
    url(r'^cars/(?P<car_id>\d+)', views.car_detail),
    url(r'^szervizkapcsolat/', include('szervizkapcsolat.urls')),
    url(r'^hahukapcsolat', include('hahu_kapcsolat.urls')),
    url(r'^flottakezeles/$',views.flottakezeles, name="flottakezeles"),
    url(r'^ajanlatkapcsolat/$',views.ajantlatkapcsi, name="ajanlatkapcsolat"),
    url(r'^forester/$',views.forester, name="forester"),
    url(r'^tivoli-akcio/$',views.tivoli, name="tivoli-akcio"),
    url(r'^eclipse-cross/$',views.eclipse, name="eclipse-cross"),
    url(r'^rexton-g4/$',views.rextong4, name="rextong4"),
    url(r'^mitsubishi-asx/$',views.asx, name="mitsu-asx"),
    url(r'^nagycsalados-7-szemelyes-auto/$',views.nagycsalados, name="nagycsalados"),



]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += [
#    url(r'^$', TemplateView.as_view(template_name='static_pages/homepage.html'), name='fooldal'),
#] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
