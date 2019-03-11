from django.db import models

# Create your models here.
# make sure this is at the top if it isn't already
from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )




class Hasznalt(models.Model):
    name = models.CharField(max_length=60)
    age = models.CharField(max_length=60)
