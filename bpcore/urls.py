from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.conf import settings


app_name ='autolista'

urlpatterns = [
    url(r'^$',views.ujautok, name="ujautok"),
    url(r'^(?P<slug>[\w-]+)/$', views.ujautok_detail, name="detail"),

]


#the slug is can be anything you want
