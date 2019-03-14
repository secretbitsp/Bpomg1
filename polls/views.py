from django.shortcuts import render
# Create your views here.
from .forms import ContactForm


def szervizcontact(request):
    template = "szervizbejentkezes.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    context = {
        'form':form,
    }
    return render(request, template, context)
