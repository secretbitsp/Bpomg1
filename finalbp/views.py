from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpRequest
from xml.dom import minidom
#from xml.etree.ElementTree import ElementTree
from urllib.request import Request, urlopen, URLError
import urllib.request
import xml.etree.ElementTree as et
import urllib.request
# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
import xmltodict
import json
from django.shortcuts import render
from .forms import RegCarForm
import sqlite3
from finalbp.models import Blog

def homepage(request):
   return render(request,'homepage.html')



def szerviz(request):
    return render(request,'szerviz.html')



def hello2(request):
    file = urllib.request.urlopen('https://www.brics.dk/ixwt/exercises/students.xml')
    data = file.read()
    xml_data = et.fromstring(data)
    print(xml_data)
    file.close()
    #data = json.dumps(xmltodict.parse(data))
    student = xml_data.findall("./student")
    print("Found %s student." % len(student))
    #list_dict = []
    for base_category in student:
        name = base_category.find("name").text
        #list_dict.append({
        #    "name": base_category.find("name").text,
        #    "age": int(base_category.find("age").text),
        #})
    b = Blog(name=name, tagline='All the latest Beatles news.')
    b.save()
    details = Blog.objects.all()

    #    list_dict.append({
    #        "name": base_category.find("name").text,
    #        "age": int(base_category.find("age").text),
    #    })

    #data2 = json.dumps(list_dict)
    print("Data updated")
    #print(data2)
    return render(request, 'hasznaltauto.html', {'data': details})



def regcar(request):
    if request.method == 'POST':
        car_form = RegCarForm(data=request.POST)

        if car_form.is_valid():
            cdata = car_form.cleaned_data.get
            car_selected = Car.objects.filter(name=cdata('car_select'))
            reg1 = Fleet(car_id=car_selected[0].id, description=cdata('description'))
            reg1.save()
        else:
            print ('Invalid')

    else:
        car_form = RegCarForm()
    return render(request, 'ajanlatok.html', {'car_form': car_form})
