from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(label='name')
    email = forms.CharField(label='email')
    phone = forms.CharField(label='phone', required = False)
    message = forms.CharField(label='message')