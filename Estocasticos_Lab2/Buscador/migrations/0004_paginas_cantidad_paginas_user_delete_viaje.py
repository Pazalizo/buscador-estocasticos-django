# Generated by Django 4.2.1 on 2023-05-24 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Buscador', '0003_paginas_viaje_delete_preferencias_delete_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginas',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paginas',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Viaje',
        ),
    ]