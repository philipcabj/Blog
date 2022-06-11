from django import forms
from .models import Post

class Formulario_usuarios(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nac = forms.DateField()


class Formulario_noticias(forms.Form):
    titulo = forms.CharField(max_length=40)
    nota = forms.CharField(max_length=100)
    fecha = forms.DateField()


class Formulario_valoracion(forms.Form):
    puntaje = forms.IntegerField()
    comentarios = forms.CharField(max_length=100)




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'texto',)