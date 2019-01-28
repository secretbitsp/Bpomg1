from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.homepage),
    url(r'^kapcsolat/$',views.contact),

]
