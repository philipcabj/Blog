from datetime import timezone
from unicodedata import name
from django.http import HttpResponse
from django.http import request
from django.shortcuts import redirect, render
from Web.models import Usuarios
from django.shortcuts import render, get_object_or_404
from Web.models import Usuarios, Post, Valoracion
from django.template import loader
from Web.forms import Formulario_usuarios, Formulario_noticias, Formulario_valoracion
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm
from django.shortcuts import redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.views import LogoutView



# Create your views here.

def inicio (request):
    
    return render(request, "padre.html")

#@login_required
def usuario (request):
    users = Usuarios.objects.all()
    tabla = {"Usuarios" : users}
    plantilla = loader.get_template("usuarios.html")
    documento = plantilla.render(tabla)
    return HttpResponse(documento)

def alta_usuarios(request):
    usuarios = Usuarios(nombre="Ulises", apellido="Guarino", edad=4, fecha_nac="2017-12-26")
    usuarios.save()
    texto = f"Se guardo en la BD: {usuarios.nombre} Apellido: {usuarios.apellido} Edad: {usuarios.edad} Fecha de Nacimiento: {usuarios.fecha_nac}"
    return HttpResponse(texto)


def alumnos(request):
    
    return render(request, "alumnos.html")

def contacto(request):
    
    return render(request, "contacto.html")


def alta_usuarios(request):

    if request.method == "POST":

        mi_formulario = Formulario_usuarios( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
        usuario = Usuarios(nombre=datos['nombre'] , apellido=datos['apellido'], edad=datos['edad'] , fecha_nac=datos['fecha_nac'])
        usuario.save()
    
        return render( request, "formulario.html")
        
    return render( request, "formulario.html")


def login_request (request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)
                return render(request, "padre.html", {"form":form})

        else:
            return HttpResponse("Usuario Incorrecto")

    else:
       # return HttpResponse(f"FORM INCORRECTO, {form}")


     form = AuthenticationForm()

    return render(request, "login.html", {"form":form})


def registro(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("Usuario Creado")
            #return redirect('padre', foo='bar')
            return render(request, "padre.html", {"form":form})
            #return messages.success(request, 'Usuario creado con exito!')

    else:
        form = UserCreationForm()
        
    return render(request, "registro.html", {"form":form})


def buscar_post (request):
    
    return render(request, "busqueda_post.html")

def buscar (request):

    if request.GET['titulo']:
        titulo = request.GET['titulo']
        post = Post.objects.filter(titulo__icontains = titulo)
        return HttpResponse(Post)
    else:
        return HttpResponse("CAMPO VACIO")

    return HttpResponse(f"Estamos buscar un post:  {request.GET['titulo']}")


def post_new(request):
    
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.fecha_publicacion = timezone.now()
                post.save()
                return redirect('post_detalle', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'formulario_post.html', {'form': form})


def post_list(request):

    #posts = Post.objects.all()
    posts = Post.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')
    return render(request, 'post_list.html', {'post': posts})


def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detalle.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('post_detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

