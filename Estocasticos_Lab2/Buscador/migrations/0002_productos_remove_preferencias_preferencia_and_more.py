# Generated by Django 4.2.1 on 2023-05-22 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buscador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='preferencias',
            name='preferencia',
        ),
        migrations.AlterField(
            model_name='preferencias',
            name='cant',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='preferencias',
            name='productos',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Buscador.productos'),
        ),
    ]
