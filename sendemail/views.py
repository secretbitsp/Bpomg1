from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # Add this
from django.core.mail import send_mail
from .forms import ContactForm # Add this





# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def kapcsolat(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['név']
            sender_email = form.cleaned_data['email']
            message = "{0} nevü ügyfelünk üzenetet küldött neked:\n\n{1}".format(sender_name, sender_email, form.cleaned_data['üzenet'])
            send_mail('Új ügyfélkapcsolat a weboldalról', message, sender_email, [settings.EMAIL_HOST_USER])
            return HttpResponse('Üzeneted elküldve!')
    else:
        form = ContactForm()

    return render(request, 'sendemail/kapcsolat.html', {'form': form})

#    return render(request, "sendemail/email.html", {'form': form})
