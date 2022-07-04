from re import template
from django import urls
from django.urls import URLPattern, path, re_path
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    path("about", views.about, name="about"), # contacto sin usar
    path("alta_usuarios", views.alta_usuarios), # Alta usuarios sin usar
    path("registro", views.registro, name="registro"), # Registro de usuarios
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="logout"), # logout
    path("login" , LoginView.as_view(template_name="login.html") , name="login"), # login
    path('post_new', views.post_new, name='post_new'), # Crear posts
    path('post_list', views.post_list, name='post_list'), # Listar posts
    path('lista_post', views.lista_post, name='lista_post'), # Listar posts
    re_path(r'^eliminar_post', views.eliminar_post, name='eliminar_post'), # Eliminar post
    path("list_users", views.list_users, name="list_users"),# Listar Usuarios
    re_path(r'^edit_user/(?P<id>\d+)/$', views.edit_user, name='edit_user'), # Editar Usuarios
    re_path(r'^eliminar_user/(?P<id>\d+)/$', views.eliminar_user, name='eliminar_user'), # Eliminar Usuarios
    path('post/<int:pk>/', views.post_detalle, name='post_detalle'), # Detalle de Posts
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # Editar Post
    #path('post/new/', views.post_new, name='post_new'), # Viejo
    #path('post/<int:pk>/comentario/$', views.agregar_comentario, name='agregar_comentario'),
    re_path(r'^post/(?P<pk>[0-9]+)/comment/$', views.agregar_comentario, name='agregar_comentario'), # Agregar Comentario a post
    re_path(r'^comentario/(?P<pk>[0-9]+)/aprovado/$', views.comentario_aprovado, name='comentario_aprovado'), # Aprovar Comentario / No funciona correctamente
    re_path(r'^comentario/(?P<pk>[0-9]+)/removido/$', views.comentario_removido, name='comentario_removido'), # Remover Comentario
    path('toggle-status', views.toggle_status, name='toggle-status'),
    #re_path(r'^comentario/(?P<pk>\d+)/aprovado/$', views.comentario_aprovado, name='comentario_aprovado'),
    #re_path(r'^comentario/(?P<pk>\d+)/removido/$', views.comentario_removido, name='comentario_removido'),
    path("", views.post_list), # HOME


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

