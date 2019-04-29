from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import hasznaltkapcsolat



def hasznaltkapcsi(request):
    if request.method == 'POST':
        form = hasznaltkapcsolat(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['név']
            sender_email = form.cleaned_data['email']
            sender_phone = form.cleaned_data['telefonszám']
            message = "{0}  ügyfelünk üzenetet küldött neked:\n\n{1}".format(sender_name, sender_email, sender_phone, form.cleaned_data['üzenet'])
            send_mail('Új ügyfélkapcsolat a weboldalról', message, 'varga.laszlo@budapestautoszalon.hu', ['kovacs.ferenc@opelsziget.hu'],)
            return render(request, 'hahu_kapcsolat/hahukapcsolat.html', {'form': form})
    else:
        form = hasznaltkapcsolat()

    return render(request, 'hahu_kapcsolat/hahukapcsolat.html', {'form': form})
