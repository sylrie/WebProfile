from django import forms

class ContactForm(forms.Form):
    #code = forms.CharField(label='code', max_length='5')
    name = forms.CharField(label='name')
    email = forms.CharField(label='email')
    phone = forms.CharField(label='phone')
    message = forms.CharField(label='message')