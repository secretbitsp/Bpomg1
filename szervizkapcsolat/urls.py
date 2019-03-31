from django.contrib import admin
from django.conf.urls import url
from . import views
from django.conf import settings

app_name ='szervizkap'

urlpatterns = [
    url(r'^$',views.szervizkapcsi, name="szervizkapcsi"),
]
