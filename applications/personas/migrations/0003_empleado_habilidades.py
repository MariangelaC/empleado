# Generated by Django 3.2.3 on 2021-06-02 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20210601_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='personas.Habilidades'),
        ),
    ]
