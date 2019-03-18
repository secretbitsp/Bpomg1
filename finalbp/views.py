from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpRequest
from xml.dom import minidom
#from xml.etree.ElementTree import ElementTree
from urllib.request import Request, urlopen, URLError
import urllib.request
import urllib.request
# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.shortcuts import render
from .forms import RegCarForm
from .models import Hahudeta

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
    #file = urllib.request.urlopen('http://hex.hasznaltauto.hu/1.0/xml/alphamobil_hex')
    #tree = ET.ElementTree()
    #tree.parse(file)
    #root = tree.getroot()
    #ET.dump(tree)
    #for elem in tree.iter():
    #    print (elem.tag, elem.attrib)
    #Hahuautok.objects.all().delete()
    #x = root.iter('{http://hex.hasznaltauto.hu/ns}kep')
    #for k in x:
    #    kep = k.get('kicsi')
        #b = Hahuautok.objects.create(kep=kep)
        #b.save()
    #x = root.iter('{http://hex.hasznaltauto.hu/ns}hirdetes')
    #for autok in x:
    #        rank = autok.get('hirdeteskod')
    #        marka = autok.get('gyartmany')
    #        kategoria = autok.get('kategoria')
    #        modell = autok.get('modell')
    #        tipus = autok.get('tipus')
    #        print(tipus)
            #a = Hahudeta.objects.create(rank=rank, marka=marka, kategoria=kategoria, modell=modell, tipus=tipus)
            #a.save()
    kep_list = Hahuautok.objects.filter()[:5]
    contact_list = Hahudeta.objects.get_queryset().order_by('id')
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    data = paginator.get_page(page)
    print("Data updated")
    return render(request, 'hasznaltauto.html', {'data': data, 'kepek' : kep_list})











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
