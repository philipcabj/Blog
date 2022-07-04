from distutils.command.upload import upload
from email.policy import default
from operator import truediv
from django.conf import settings
from django.db import models
from django.utils import timezone
from Blog.settings import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField



# Create your models here.
class Usuarios(AbstractUser):
    foto = models.ImageField(upload_to= 'images/', null=True, blank=False, default='avatar.png')
    

    def getImage (self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'images/avatar.png')
    
    class Meta:
        ordering = ['id']

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto= RichTextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)
    #like = models.ManyToManyField(User, blank="True", related_name='likes')
    #dislike = models.ManyToManyField(User, blank="True", related_name='likes')
    class Meta:
        ordering = ['id']

    def Comentarios_aprovados(self):
        return self.Comentarios_aprovados.filter(comentario_aprovado=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
class Comentarios(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=200)
    texto = RichTextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    comentario_aprovado = models.BooleanField(default=False)

    def approve(self):
        self.comentario_aprovado = True
        self.save()

    def __str__(self):
        return self.texto

