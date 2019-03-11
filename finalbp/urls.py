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
    url(r'^hasznaltauto/$',views.regcar, name="hasznalt"),
    url(r'^kapcsolat/', include('sendemail.urls')),
    #url(r'^feeds/models-by-make-id/(\d+)/$', 'autos.views.feed_models'),



]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += [
#    url(r'^$', TemplateView.as_view(template_name='static_pages/homepage.html'), name='fooldal'),
#] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
