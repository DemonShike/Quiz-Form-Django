from django.db import models

# Create your models here.

class Formulario(models.Model):
    nickname = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    uid = models.CharField(max_length=20)
    level = models.IntegerField()
    gamemode = models.CharField(max_length=50)
    element_fav = models.CharField(max_length=20)
    about_tower = models.CharField( max_length=50)
    usually_tof = models.CharField( max_length=50)
    like_about = models.TextField()