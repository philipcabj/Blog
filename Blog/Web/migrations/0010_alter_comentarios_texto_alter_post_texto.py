# Generated by Django 4.0.4 on 2022-06-28 18:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0009_alter_usuarios_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='texto',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]