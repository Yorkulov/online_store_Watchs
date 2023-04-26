from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import models
from account.models import Profile, ContactModel, CommentModel

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password",
                               help_text="Your password must be at least 8 characters long.",
                               widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Return Password",
                                 help_text="Repeat the above password here as well.",
                                 widget=forms.PasswordInput)
    
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': "You can only use numbers and letters when choosing a username",
        }
        
    def clean_password_2(self):
        data = self.cleaned_data
        if data['password'] != data['password_2']:
            raise forms.ValidationError('Ikkala maydondagi parollar birbiriga mos kelishi kerak!')
        return data['password_2']
    

class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['gender', 'date_of_birth', 'image']


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactModel
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['text']
