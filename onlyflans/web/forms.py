from socket import fromshare
from django import forms
from .models import ContactForm, Flan
from django.forms import ModelForm, RadioSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactFormForm(forms.Form):
    
    customer_email=forms.EmailField(label='Correo')
    customer_name=forms.CharField(max_length=64,label='Nombre')
    message= forms.CharField(label='Mensaje')

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email','customer_name','message']

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label = "Correo electrónico")
    username = forms.CharField(label = "Nombre de usuario")
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)
    

    class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2' ]


            