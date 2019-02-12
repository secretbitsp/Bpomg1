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
# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

def homepage(request):
   return render(request,'homepage.html')

#def contact(request):
#    return render(request,'kapcsolat.html')

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
        print('---------')
        print(headers)
        data = response.read().decode('utf-8')
        print('LENGTH  :', len(data))
        print('DATA    :')
        print('---------')
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



# our view
# add to the top
from finalbp.forms import ContactForm

# add to your views
# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template =get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['yepense@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('kapcsolat')

    return render(request, 'kapcsolat.html', {
        'form': form_class,
    })
