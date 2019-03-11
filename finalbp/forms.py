
# make sure this is at the top if it isn't already
from django import forms
import json
from django import forms
from .models import *


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label ="What do you want to say?"



class RegCarForm(forms.ModelForm):
    dcars = {}
    list_cars = []
    for car in Car.objects.all():
        if car.brand.company_name in dcars:
            dcars[car.brand.company_name].append(car.name)
        else:
            dcars[car.brand.company_name] = [car.name]
        list_cars.append((car.name,car.name))

    brands = [str(brand) for brand in Brand.objects.all()]

    brand_select = forms.ChoiceField(choices=([(brand, brand) for brand in brands]))
    car_select = forms.ChoiceField(choices=(list_cars))

    brands = json.dumps(brands)
    cars = json.dumps(dcars)

    class Meta:
        model = Fleet
        fields = ('brand_select', 'car_select', 'description',)
