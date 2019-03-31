from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['Vezetéknév'].widget.attrs.update({'class' : 'form-control'})
        self.fields['Email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['Telefonszám'].widget.attrs.update({'class' : 'form-control'})
        self.fields['Üzenet'].widget.attrs.update({'class' : 'form-control'})
