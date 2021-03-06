import datetime
import os
from .models import Hahudeta, CachedImage
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import urllib.request


def fetch_cars():
    '''
    file = urllib.request.urlopen('http://hex.hasznaltauto.hu/1.0/xml/alphamobil_hex')
    tree = ET.ElementTree()
    tree.parse(file)'''
    tree = ET.parse('alphamobil_hex.xml')
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
    Hahudeta.objects.all().delete()
    CachedImage.objects.all().delete()
    print("Deleted database ")
    print("Loading the new cars")
    print("3")
    print("2")
    print("1")
    print("Adatbázis frissitése")
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
            print(rank)
            uzemanyag = autok.findall('{http://hex.hasznaltauto.hu/ns}uzemanyag')
            if uzemanyag:
                uzemanyag = uzemanyag[0].text
            else:
                uzemanyag = None
            evjarat = autok.findall('{http://hex.hasznaltauto.hu/ns}evjarat')[0].text
            if ('/' in evjarat):
                evjarat = datetime.datetime.strptime(evjarat, '%Y/%m')
            else:
                evjarat = datetime.datetime.strptime(evjarat, '%Y')
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
            try:
                futottkm = autok.findall('{http://hex.hasznaltauto.hu/ns}futottkm')[0].text
            except IndexError:
                futottkm = None
            ar = autok.findall('{http://hex.hasznaltauto.hu/ns}ar')[0].text
            allapot = autok.findall('{http://hex.hasznaltauto.hu/ns}allapot')[0].text
            try:
                email = autok.findall('{http://hex.hasznaltauto.hu/ns}emailcim')[0].text
            except IndexError:
                email = None
            print(ar)
            Hahudeta.objects.filter(rank=rank).delete()
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
            print("Deleted database ")
            print("Loading the new cars")
            print("3")
            print("2")
            print("1")
            print("Adatbázis frissitése")
            filename = os.path.basename(url)
            car_code = filename.split('_')[0]
            car = cars.get(car_code)
            if not car:
                continue
            # image = urlretrieve(url)
            cached_image = CachedImage.objects.create(url=url, car=car)
