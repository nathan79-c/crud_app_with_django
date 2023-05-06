from django import forms

class ContactUsForms(forms.Form):
    name = forms.CharField(required=False)
    email =forms.EmailField()
    message = forms.CharField( max_length=1000, required=True)