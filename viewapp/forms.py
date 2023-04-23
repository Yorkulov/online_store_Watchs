from django import forms
from .models import ContactModel, WatchRegistrationModel, WatchBuyModel


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactModel
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']


class WatchregistrationForm(forms.ModelForm):

    class Meta:
        model = WatchRegistrationModel
        fields = ['watch_number', 'country', 'address']


class WatchBuyForm(forms.ModelForm):

    class Meta:
        model = WatchBuyModel
        fields = ['card_number', 'check_code']