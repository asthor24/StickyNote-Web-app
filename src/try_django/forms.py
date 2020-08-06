from django import forms

class ContactForm(forms.Form):
    full_name =forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput())
