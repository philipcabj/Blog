# Generated by Django 4.0.4 on 2022-06-24 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0008_alter_usuarios_options_alter_usuarios_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='foto',
            field=models.ImageField(default='images/avatar.png', null=True, upload_to='images/'),
        ),
    ]
