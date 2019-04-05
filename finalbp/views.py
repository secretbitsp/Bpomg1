import os
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpRequest, HttpResponseRedirect
from xml.dom import minidom
#from xml.etree.ElementTree import ElementTree
from urllib.request import Request, urlopen, URLError, urlretrieve
import urllib.request
# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.shortcuts import render
from .models import Hahudeta, CachedImage
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from django.core.paginator import Paginator
from .models import Hahuautok

def homepage(request):
   return render(request,'homepage.html')



def szerviz(request):
    return render(request,'szerviz.html')



def hello2(request):
    file = urllib.request.urlopen('http://hex.hasznaltauto.hu/1.0/xml/alphamobil_hex')
    tree = ET.ElementTree()
    tree.parse(file)
    root = tree.getroot()
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
    x = root.iter('{http://hex.hasznaltauto.hu/ns}hirdetes')
    cars = {}
    for autok in x:
            #print([elem.tag for elem in autok.iter()])
            #print(autok.findall('{http://hex.hasznaltauto.hu/ns}uzemanyag'))
            rank = autok.get('hirdeteskod')
            marka = autok.get('gyartmany')
            kategoria = autok.get('kategoria')
            modell = autok.get('modell')
            tipus = autok.get('tipus')
            uzemanyag = autok.findall('{http://hex.hasznaltauto.hu/ns}uzemanyag')
            if uzemanyag:
                uzemanyag = uzemanyag[0].text
            else:
                uzemanyag = None
            evjarat = autok.findall('{http://hex.hasznaltauto.hu/ns}evjarat')[0].text
            felszereltseg = autok.findall('{http://hex.hasznaltauto.hu/ns}felszereltseg')[0].text
            Telefonszám = autok.findall('{http://hex.hasznaltauto.hu/ns}telefonszam_1')[0].text
            futottkm = autok.findall('{http://hex.hasznaltauto.hu/ns}futottkm')[0].text
            a = Hahudeta.objects.create(rank=rank, marka=marka, kategoria=kategoria, modell=modell, tipus=tipus, uzemanyag=uzemanyag, evjarat=evjarat, futottkm=futottkm,
                                        felszereltseg=felszereltseg)
            a.save()
            cars[rank] = a
    x = root.iter('{http://hex.hasznaltauto.hu/ns}kep')
    for k in x:
        url = k.get('kozepes')
        filename = os.path.basename(url)

        car_code = filename.split('_')[0]
        car = cars.get(car_code)
        if not car:
            continue
        image = urlretrieve(url)
        cached_image = CachedImage.objects.create(url=url, car=car)
    ''''
    for image in car.images.all():
        # print(image.photo.url)
        #cached_image.photo.save(filename, File(open(image[0], errors='ignore')))
        kepdocument = k.get('kozepes')
        b = pictures.objects.create(kepdocument=imagefile)
        b.save()
        newdoc = Document(imagefile=request.FILES['imagefile'])
        newdoc.save()
        latest_documents = Document.objects.all().order_by('-id')[0]'''
    make = request.GET.get('make')
    model = request.GET.get('model')
    contact_list = Hahudeta.objects.all()
    if make:
        contact_list = contact_list.filter(marka=make)
    if model:
        contact_list = contact_list.filter(modell=model)

    paginator = Paginator(contact_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    data = paginator.get_page(page)
    print("Data updated")
    makes = list(set(Hahudeta.objects.values_list('marka',  flat=True)))
    if make:
        models = list(set(Hahudeta.objects.filter(marka=make).values_list('modell', flat=True)))
    else:
        models = list(set(Hahudeta.objects.values_list('modell', flat=True)))
    return render(request, 'hasznaltauto.html', {'data': data, 'makes': makes, 'models': models, 'selected_make': make, 'selected_model': model })


def car_detail(request, car_id):
    try:
        print(car_id)
        car = Hahudeta.objects.get(id=car_id)
    except Hahudeta.DoesNotExist:
        return HttpResponseRedirect('/hahudeta')
    return render(request, 'car_detail.html', {'car': car})






#carouselExampleControls-{{e.id}}
