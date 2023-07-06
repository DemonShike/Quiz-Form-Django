# Generated by Django 4.1.7 on 2023-02-16 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('uid', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
                ('gamemode', models.CharField(max_length=50)),
                ('element_fav', models.CharField(max_length=20)),
                ('about_tower', models.CharField(max_length=50)),
                ('usually_tof', models.CharField(max_length=50)),
                ('like_about', models.TextField()),
            ],
        ),
    ]
