from django import forms

class HahuKapcsolat(forms.Form):
    név = forms.CharField(max_length=100)
    telefonszám = forms.IntegerField()
    email = forms.EmailField()
    üzenet = forms.CharField(widget=forms.Textarea)
