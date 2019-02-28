from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse # Add this
from django.core.mail import send_mail

from .forms import ContactForm # Add this



# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

# our view
def kapcsolat(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            # Email the profile with the
            # contact information
            template =get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['yepense@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()

            return redirect('/kapcsolat/')

    return render(request, 'sendemail/kapcsolat.html', {'form': form_class,})
