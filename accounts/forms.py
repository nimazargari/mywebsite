from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text',
                                                                       'placeholder': 'Username', 'name': 'username',
                                                                       'autocomplete': 'off'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text',
                                                                    'placeholder': 'Email', 'name': 'email',
                                                                    'autocomplete': 'off'}))
    password = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password',
                                                                       'placeholder': 'Password', 'name': 'password'}))
    c_password = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password',
                                                               'placeholder': 'Confirm Password', 'name': 'password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This Email Is Exist')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This Username Is Exist')
        return username

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('c_password')

        if p1 and p2 and p1 != p2:
            raise ValidationError('Passwords Not Match')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text',
                                                                       'placeholder': 'Email Or Username', 'name': 'username',
                                                                       'autocomplete': 'off'}))

    password = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password',
                                                                       'placeholder': 'Password', 'name': 'password'}))
