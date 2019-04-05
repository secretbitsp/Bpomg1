from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse # Add this
from django.core.mail import send_mail

from .forms import szervizkapcsolat2



def szervizkapcsi(request):
    if request.method == 'POST':
        form = szervizkapcsolat2(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['név']
            sender_email = form.cleaned_data['email']
            sender_phone = form.cleaned_data['telefonszám']
            message = "{0}  ügyfelünk üzenetet küldött neked:\n\n{1}".format(sender_name, sender_email, sender_phone, form.cleaned_data['üzenet'])
            send_mail('Új ügyfélkapcsolat a weboldalról', message, 'varga.laszlo@budapestautoszalon.hu', ['varga.laszlo@budapestautoszalon.hu'],)
            return HttpResponse('Thanks for contacting us!')
    else:
        form = szervizkapcsolat2()

    return render(request, 'szervizkapcsolat/szervizkapcsolat.html', {'form': form})
