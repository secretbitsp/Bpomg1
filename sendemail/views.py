from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse # Add this
from django.core.mail import send_mail

from .forms import ContactForm # Add this





# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def kapcsolat(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Név = form.cleaned_data['Név']
            Email = form.cleaned_data['Email']
            Üzenet = form.cleaned_data['Üzenet']
            try:
                send_mail(Név, Email, Üzenet, ['yepense@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #return redirect('')
    return render(request, "sendemail/email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
