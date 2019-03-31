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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['név']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['üzenet'])
            send_mail('New Enquiry', message, sender_email, ['yepense@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'sendemail/kapcsolat.html', {'form': form})

#    return render(request, "sendemail/email.html", {'form': form})
