# Generated by Django 3.2.3 on 2021-06-01 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
