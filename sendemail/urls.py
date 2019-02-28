from django.contrib import admin
from django.conf.urls import url
from . import views
from django.conf import settings

app_name ='kapcsolat'

urlpatterns = [
    url(r'^$',views.kapcsolat, name="kapcsolat"),

]
