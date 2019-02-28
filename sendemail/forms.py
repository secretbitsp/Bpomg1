from django import forms


class ContactForm(forms.Form):
    Név = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    Email = forms.EmailField(required=True)
    Üzenet = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
