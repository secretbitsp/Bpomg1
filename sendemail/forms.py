from django import forms


class ContactForm(forms.Form):
    Név = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Üzenet = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
