from re import template
from django.urls import URLPattern, path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [

    #path("", views.inicio),
    path("usuarios", views.usuario, name="usuarios"),
    path("noticias", views.alumnos, name="alumnos"),
    path("contacto", views.contacto, name="contacto"),
    #path("alta", views.alta),
    path("alta_usuarios", views.alta_usuarios),
    path("login", views.login_request, name="login"),
    path("registro", views.registro, name="registro"),
    path("buscar_post", views.buscar_post),
    path("buscar", views.buscar),
    path("loguot", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('post_new', views.post_new, name='post_new'),
    path('post_list', views.post_list, name='post_list'),
    #path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detalle, name='post_detalle'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path("", views.inicio)

]

