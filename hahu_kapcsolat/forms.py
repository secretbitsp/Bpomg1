from django import forms

class hasznaltkapcsolat(forms.Form):
    név = forms.CharField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    telefonszám = forms.IntegerField( widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    üzenet = forms.CharField( widget=forms.Textarea(attrs={'class' : 'form-control'}))
