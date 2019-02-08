from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpRequest
from xml.dom import minidom
#from xml.etree.ElementTree import ElementTree
from urllib.request import Request, urlopen, URLError
import urllib.request
from bs4 import BeautifulSoup
import xml.etree.ElementTree as etree
import socket
import urllib.request

def homepage(request):
   return render(request,'homepage.html')

def contact(request):
    return render(request,'kapcsolat.html')

def szerviz(request):
    return render(request,'szerviz.html')

#def ujautok(request):
#    return render(request,'ujautok.html')
#


#def hello2(request):
#    file = minidom.parse(urllib.request.urlopen('http://hex.hasznaltauto.hu/1.0/xml/szszigetautohaz_hex '))
#    olvas = file.read()
#    xmldoc = minidom.parseString(olvas)
#    return render('hasznaltauto.html', {'adat': xmldoc})

#Python code to illustrate parsing of XML files
# importing the required modules


def hello2(request):
    context_dict = {}
    #url = Request("http://hex.hasznaltauto.hu/1.0/xml/szszigetautohaz_hex ")
    try:
        # timeout in seconds
        #timeout = 10
        # socket.setdefaulttimeout(timeout)
        url = "http://hex.hasznaltauto.hu/1.0/xml/szszigetautohaz_hex "
        assembled_request = urllib.request.Request(url)
        response = urllib.request.urlopen(assembled_request)
        print('RESPONSE:', response)
        print('URL     :', response.geturl())
        data_content = response.read()
        soup = BeautifulSoup(data_content, features="html.parser")
        genTable = soup
        headers = response.info()
        print('DATE    :', headers['date'])
        print('HEADERS :')
        print('---------------------------------')
        print(headers)
        data = response.read().decode('utf-8')
        print('LENGTH  :', len(data))
        print('DATA    :')
        print('---------Lencsi-----------------')
        print(data)
        context_dict['genTable'] = genTable
        print(genTable)
    except URLError as e:
        if hasattr(e, 'reason'):
            print ('We failed to reach a server')
            print ('Reason: '), e.reason
        elif hasattr(e, 'code'):
            print ('The server couldn\'t fulfill the request.')
            print ('Error code: '), e.code
    else:
        print("fine")
        return render(request,'hasznaltauto.html', context_dict)
