from django.contrib import admin
from django.conf.urls import url
from . import views
from django.conf import settings

app_name ='hahukap'

urlpatterns = [
    url(r'^$',views.hasznaltkapcsi, name="hahukapcsi"),


]


#the slug  can be anything you want
