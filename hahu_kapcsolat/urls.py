from django.contrib import admin
from django.conf.urls import url
from . import views
from django.conf import settings

app_name ='HahuKapcsolat'

urlpatterns = [
    url(r'^$',views.contact_us, name="HahuKapcsolat"),
]


#the slug  can be anything you want
