from django import forms


class ContactForm(forms.Form):
    Név = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Email = forms.EmailField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Üzenet = forms.EmailField( widget=forms.Textarea(attrs={'class' : 'form-control'}))
