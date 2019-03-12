from django import forms


class ContactForm(forms.Form):
    Név = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Üzenet = forms.EmailField(required=True, widget=forms.Textarea(attrs={'class' : 'form-control'}))


class AjanlatKeres(forms.Form):
    Név = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Telefonszám = forms.CharField(max_length=12)
    Email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Üzenet = forms.EmailField(required=True, widget=forms.Textarea(attrs={'class' : 'form-control'}))
