from dataclasses import field
from django import forms
from .models import Comentarios, Post, Usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Formulario_usuarios(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nac = forms.DateField()
    foto = forms.ImageField()


class Form_Users(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuarios
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2','foto']
        help_texts = {k:"" for k in fields}



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'texto',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = ('autor', 'texto',)