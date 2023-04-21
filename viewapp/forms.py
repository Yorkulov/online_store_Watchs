from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactModel
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']