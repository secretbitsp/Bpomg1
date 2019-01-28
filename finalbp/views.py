from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'homepage.html')

def contact(request):
    return render(request,'kapcsolat.html')
