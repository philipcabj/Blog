# Generated by Django 4.0.4 on 2022-07-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0013_alter_usuarios_options_alter_usuarios_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='foto',
            field=models.ImageField(default='avatar.png', null=True, upload_to='media/images/'),
        ),
    ]
