from datetime import timezone
from email import message
from unicodedata import name
from django.http import HttpResponse
from django.http import request
from django.shortcuts import redirect, render
from Web.models import Usuarios
from django.shortcuts import render, get_object_or_404
from Web.models import Usuarios, Post, Comentarios
from django.template import loader
from Web.forms import Formulario_usuarios, Form_Users
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm, PostForm
from django.shortcuts import redirect
from .models import Comentarios, Post
from django.utils import timezone
from django.contrib.auth.views import LogoutView
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse_lazy




# Create your views here.

def inicio (request):
    
    return render(request, "padre.html")

@login_required
def usuario (request):
    users = Usuarios.objects.all()
    tabla = {"usuarios" : users}
    plantilla = loader.get_template("usuarios.html")
    documento = plantilla.render(tabla)
    return HttpResponse(documento)

def list_users(request):
    queryset = request.GET.get("buscar")

    usuarios = Usuarios.objects.all()

    if queryset:
        usuarios = Usuarios.objects.filter(Q(first_name__icontains = queryset) | Q(username__icontains = queryset)).distinct()

    paginacion = Paginator(usuarios, 20)
    pagina = request.GET.get('page')
    usuarios = paginacion.get_page(pagina)


    return render(request, 'usuarios.html', {'usuarios': usuarios})

"""def alta_usuarios(request):
    usuarios = Usuarios(nombre="Ulises", apellido="Guarino", edad=4, fecha_nac="2017-12-26")
    usuarios.save()
    texto = f"Se guardo en la BD: {usuarios.nombre} Apellido: {usuarios.apellido} Edad: {usuarios.edad} Fecha de Nacimiento: {usuarios.fecha_nac}"
    return HttpResponse(texto)"""




def about(request):
    
    return render(request, "about.html")




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
                return render(request, "post_list.html", {"form":form})

        else:
            return HttpResponse("Usuario Incorrecto")

    else:

     form = AuthenticationForm()

    return render(request, "login.html", {"form":form})



def registro(request):

    if request.method == "POST":   
        form = Form_Users(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con exito')
            return redirect('post_list')
    else:
        form = Form_Users()     
    return render(request, "registro.html", {"form":form})

def edit_user (request, id):
    user = Usuarios.objects.get(id=id)
    if request.method == "GET":
        form = Form_Users(instance=user)
    else:
        form = Form_Users(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('list_users')
    return render(request, 'registro.html', {'form':form})

@login_required
def eliminar_user(request, id):
    user = Usuarios.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect('list_users')
    return render(request, 'eliminar_user.html')


def eliminar_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect('lista_post')
    return render(request, 'eliminar_post.html')
   

@login_required
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

@login_required
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
    
    queryset = request.GET.get("buscar")
    #posts = Post.objects.all()
    posts = Post.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')

    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(texto__icontains = queryset)).distinct()
    
    paginacion = Paginator(posts, 3)
    pagina = request.GET.get('page')
    posts = paginacion.get_page(pagina)

    return render(request, 'post_list.html', {'post': posts})

def lista_post(request):
    
    queryset = request.GET.get("buscar")
    #posts = Post.objects.all()
    posts = Post.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')

    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(texto__icontains = queryset)).distinct()
    
    paginacion = Paginator(posts, 3)
    pagina = request.GET.get('page')
    posts = paginacion.get_page(pagina)

    return render(request, 'lista_post.html', {'post': posts})

def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detalle.html', {'post': post})




def agregar_comentario(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detalle', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'agregar_comentario.html', {'form': form})


@login_required
def comentario_aprovado(request, pk):
    comment = get_object_or_404(Comentarios, pk=pk)
    comment.approve()
    return redirect('post_detalle', pk=comment.post.pk)

@login_required
def comentario_removido(request, pk):
    comment = get_object_or_404(Comentarios, pk=pk)
    comment.delete()
    return redirect('post_detalle', pk=comment.post.pk)


def toggle_status(request):
    return redirect(reverse_lazy('lista_post.html'))