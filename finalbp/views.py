from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'homepage.html')

def contact(request):
    return render(request,'kapcsolat.html')

def szerviz(request):
    return render(request,'szerviz.html')

#def ujautok(request):
#    return render(request,'ujautok.html')
#
