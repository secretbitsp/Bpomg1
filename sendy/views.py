
# Create your views here.
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse # Add this

from .forms import ContactForm # Add this
from django.core.mail import send_mail
