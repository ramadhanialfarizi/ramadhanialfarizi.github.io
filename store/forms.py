from django.contrib.auth import password_validation
from store.models import Address
from django import forms
import django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from django.utils.translation import gettext, gettext_lazy as _



class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Kata Sandi', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Kata Sandi'}))
    password2 = forms.CharField(label="Konfirmasi Kata Sandi", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Konfirmasi Kata Sandi'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Alamat Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Kata Sandi"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['locality', 'city', 'state']
        widgets = {'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tempat Populer seperti Restoran, Tempat Wisata, dll'}), 'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kota'}), 'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Provinsi'})}
