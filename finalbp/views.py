import os

from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpRequest, HttpResponseRedirect
#from xml.etree.ElementTree import ElementTree
from urllib.request import Request, urlopen, URLError, urlretrieve
import urllib.request
from django.views.generic import View
from django.core.mail import send_mail
from .forms import ajanlatkapcsolat
from .forms import flottakapcsolat
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from .models import Hahudeta, CachedImage
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from django.core.paginator import Paginator
from .models import Hahuautok




def homepage(request):
   return render(request,'homepage.html')

def forester(request):
        return render(request,'bpcore/foresterlanding.html')

def tivoli(request):
        return render(request,'bpcore/landing.html')

def eclipse(request):
        return render(request,'bpcore/eclipse.html')

def nagycsalados(request):
        return render(request,'bpcore/7szemely.html')

def rextong4(request):
        return render(request,'bpcore/rextongg4.html')

def flottaajanlat(request):
        return render(request,'bpcore/flottaajanlat.html')

def asx(request):
        return render(request,'bpcore/mitsubishi-asx.html')


def flottakezeles(request):
    if request.method == 'POST':
        form = flottakapcsolat(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['név']
            sender_email = form.cleaned_data['email']
            sender_phone = form.cleaned_data['telefonszám']
            sender_mail = form.cleaned_data['megjegyzés']
            message = "{0}  Ügyfelünk üzenetet küldött neked:\n\n{1}\nTelefonszám: {2}\nÜzenet: {3}".format(sender_name, sender_email, sender_phone, sender_mail)
            send_mail('Új érdeklődés a weboldalról', message, 'info@budapestautoszalon.hu', ['flottakezeles@flottasziget.hu'],)
            print(send_mail)
            print(sender_mail)
            print(message)
            return HttpResponseRedirect('/flottakezeles')
    else:
        form = flottakapcsolat()

    return render(request,'bpcore/flottakezeles.html', {'form': form})



def szerviz(request):
    return render(request,'szerviz.html')

    '''file = urllib.request.urlopen('http://hex.hasznaltauto.hu/1.0/xml/alphamobil_hex')
    tree = ET.ElementTree()
    tree.parse(file)'''
    '''tree = ET.parse('alphamobil_hex.xml')
    root = tree.getroot()'''

def hello2(request):

    #ET.dump(tree)
    #for elem in tree.iter():
        #print (elem.tag, elem.attrib)
    #x = root.iter('{http://hex.hasznaltauto.hu/ns}hirdetes')
    #for arak in x:
        #for elem in arak.iter():

        #    print(elem.tag)
        #    if elem.tag == '{http://hex.hasznaltauto.hu/ns}uzemanyag':
        #        print(elem.text)
        # print(arak.findall('uzemanyag'))
        #print(araks)
    '''x = root.iter('{http://hex.hasznaltauto.hu/ns}hirdetes')
    cars = {}
    for autok in x:
            #print([elem.tag for elem in autok.iter()])
            #print(autok.findall('{http://hex.hasznaltauto.hu/ns}uzemanyag'))
            rank = autok.get('hirdeteskod')
            marka = autok.get('gyartmany')
            kategoria = autok.get('kategoria')
            modell = autok.get('modell')
            tipus = autok.get('tipus')
            print(rank)
            uzemanyag = autok.findall('{http://hex.hasznaltauto.hu/ns}uzemanyag')
            if uzemanyag:
                uzemanyag = uzemanyag[0].text
            else:
                uzemanyag = None
            evjarat = autok.findall('{http://hex.hasznaltauto.hu/ns}evjarat')[0].text
            try:
                hengerelrendezes  = autok.findall('{http://hex.hasznaltauto.hu/ns}hengerelrendezes')[0].text
            except IndexError:
                hengerelrendezes = None
            try:
                teljesitmeny = autok.findall('{http://hex.hasznaltauto.hu/ns}teljesitmeny')[0].text
                print(teljesitmeny)
            except IndexError:
                teljesitmeny = None
            hengerurtartalom  = autok.findall('{http://hex.hasznaltauto.hu/ns}hengerurtartalom')[0].text
            #klima  = autok.findall('{http://hex.hasznaltauto.hu/ns}klima')[1].text
            try:
                sebessegvalto   = autok.findall('{http://hex.hasznaltauto.hu/ns}sebessegvalto')[0].text
            except IndexError:
                sebessegvalto = None
            try:
                szin   = autok.findall('{http://hex.hasznaltauto.hu/ns}szin')[0].text
            except IndexError:
                szin = None
            try:
                muszaki = autok.findall('{http://hex.hasznaltauto.hu/ns}muszaki')[0].text
            except IndexError:
                muszaki = None
            try:
                leiras = autok.findall('{http://hex.hasznaltauto.hu/ns}leiras')[0].text
            except IndexError:
                leiras = None
            felszereltseg = autok.findall('{http://hex.hasznaltauto.hu/ns}felszereltseg')[0].text
            telefonszam  = autok.findall('{http://hex.hasznaltauto.hu/ns}telefonszam')[0].text
            futottkm = autok.findall('{http://hex.hasznaltauto.hu/ns}futottkm')[0].text
            ar = autok.findall('{http://hex.hasznaltauto.hu/ns}ar')[0].text
            allapot = autok.findall('{http://hex.hasznaltauto.hu/ns}allapot')[0].text
            email = autok.findall('{http://hex.hasznaltauto.hu/ns}emailcim')[0].text

            print(ar)

            a = Hahudeta.objects.create(rank=rank, marka=marka, kategoria=kategoria,
                                        modell=modell, tipus=tipus, uzemanyag=uzemanyag,
                                        evjarat=evjarat, futottkm=futottkm,
                                         telefonszam=telefonszam, ar=ar,
                                         sebessegvalto=sebessegvalto,
                                         hengerelrendezes=hengerelrendezes,
                                         allapot=allapot, teljesitmeny=teljesitmeny,
                                         muszaki=muszaki, szin=szin, email=email, leiras=leiras)
            a.save()
            cars[rank] = a
    x = root.iter('{http://hex.hasznaltauto.hu/ns}kepek')
    for k in x:
        #print(k.findall('{http://hex.hasznaltauto.hu/ns}kep'))
        for kep in k.findall('{http://hex.hasznaltauto.hu/ns}kep'):
            url = kep.text
            print(url)
            filename = os.path.basename(url)
            car_code = filename.split('_')[0]
            car = cars.get(car_code)
            if not car:
                continue
            # image = urlretrieve(url)
            cached_image = CachedImage.objects.create(url=url, car=car)'''

    make = request.GET.get('make')
    model = request.GET.get('model')
    fuel = request.GET.get('fuel')
    date = request.GET.get('date')
    price = request.GET.get('price')


    contact_list = Hahudeta.objects.order_by("marka")
    if make:
        contact_list = contact_list.filter(marka=make)
    if model:
        contact_list = contact_list.filter(modell=model)
    if fuel:
        contact_list = contact_list.filter(uzemanyag=fuel)
    if date:
        if date == '1999_less_than':
            contact_list = contact_list.filter(evjarat__year__lt=1999)
        if date == '2000_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2000)
        if date == '2001_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2001)
        if date == '2002_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2002)
        if date == '2003_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2003)
        if date == '2004_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2004)
        if date == '2005_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2005)
        if date == '2006_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2006)
        if date == '2007_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2007)
        if date == '2008_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2008)
        if date == '2009_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2009)
        if date == '2010_to_today':
            contact_list = contact_list.filter(evjarat__year__gte=2010)
    #if price:
            #contact_list = contact_list.filter(ar=price)
        #    if price == '500_less':
        #        contact_list = contact_list.filter(ar__lt=500)

    paginator = Paginator(contact_list, 25) # Show 25 car per page
    page = request.GET.get('page')
    data = paginator.get_page(page)

    dates = list(set(Hahudeta.objects.values_list('evjarat',  flat=True)))
    makes = sorted(list(set(Hahudeta.objects.order_by('marka').values_list('marka',  flat=True))))
    fuels = list(set(Hahudeta.objects.values_list('uzemanyag',  flat=True)))
    prices = list(set(Hahudeta.objects.values_list('ar',  flat=True)))


    if make:
        models = list(set(Hahudeta.objects.filter(marka=make).values_list('modell', flat=True)))
    else:
        models = list(set(Hahudeta.objects.values_list('modell', flat=True)))
        fuels = list(set(Hahudeta.objects.filter(marka=make).values_list('uzemanyag', flat=True)))
        dates = list(set(Hahudeta.objects.values_list('evjarat',  flat=True)))
        price = list(set(Hahudeta.objects.values_list('ar',  flat=True)))

    return render(request, 'hasznaltauto.html', {'data': data, 'makes': makes, 'models': sorted(models),'fuels':fuels, 'dates':dates, 'prices':prices,
                                                 'selected_make': make, 'selected_model': model, 'selected_fuel': fuel, 'selected_date' : date, 'selected_price': price})




def car_detail(request, car_id):
    try:
        print(car_id)
        car = Hahudeta.objects.get(id=car_id)
    except Hahudeta.DoesNotExist:
        return HttpResponseRedirect('/hahudeta')
    return render(request, 'car_detail.html', {'car': car})




def ajantlatkapcsi(request):
    if request.method == 'POST':
        form = ajanlatkapcsolat(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['név']
            sender_email = form.cleaned_data['email']
            sender_phone = form.cleaned_data['telefonszám']
            sender_mail = form.cleaned_data['üzenet']
            message = "{0}  Ügyfelünk üzenetet küldött neked:\n\n{1}\nTelefonszám: {2}\nÜzenet: {3}".format(sender_name, sender_email, sender_phone, sender_mail)
            send_mail('Új érdeklődés a weboldalról', message, 'info@budapestautoszalon.hu', ['kardos.tamas@mitsubishibudapest.hu'],)
            print(send_mail)
            print(sender_mail)
            print(message)
            return render(request, 'ajanlatkapcsolat.html', {'form': form})
    else:
        form = ajanlatkapcsolat()

    return render(request, 'ajanlatkapcsolat.html', {'form': form})
