# Generated by Django 4.1 on 2022-09-01 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='idade',
            field=models.IntegerField(),
        ),
    ]
