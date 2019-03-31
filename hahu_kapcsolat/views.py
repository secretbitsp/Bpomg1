from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse # Add this
from django.core.mail import send_mail

from .forms import HahuKapcsolat # Add this



def contact_us(request):
    if request.method == 'POST':
        form = HahuKapcsolat(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['név']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['üzenet'])
            send_mail('New Enquiry', message, sender_email, ['yepense@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = HahuKapcsolat()

    return render(request, 'hahu_kapcsolat/Hahu-kapcsolat.html', {'form': form})
