
from django import forms



class ajanlatkapcsolat(forms.Form):
    név = forms.CharField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    telefonszám = forms.IntegerField( widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    üzenet = forms.CharField( widget=forms.Textarea(attrs={'class' : 'form-control'}))


class flottakapcsolat(forms.Form):
    név = forms.CharField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    cégnév = forms.CharField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    telefonszám = forms.IntegerField( widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    megjegyzés = forms.CharField( widget=forms.Textarea(attrs={'class' : 'form-control'}))
