from django.shortcuts import render,HttpResponse,redirect
from miapp.models import Formulario

# Create your views here.

def form(request):

    return render(request, 'form.html')

def save(request):

    if request.method == 'GET':
        nick = request.GET["nick-name"]
        email = request.GET["email"]
        uid = request.GET["uid"]
        level = request.GET["level"]
        gamemode = request.GET["gamemode"]
        element_fav = request.GET["element_fav"]
        about_tower = request.GET["about_tower"]
        usually_tof = request.GET.getlist("usually_tof") #Con esto recibimos los datos del get en su forma de lista
        like_about = request.GET["like_about"]

        if len(usually_tof) == 0:
            usually_tof = "none"

        formulario = Formulario(
        nickname = nick,
        email = email,
        uid = uid,
        level = level,
        gamemode = gamemode,
        element_fav = element_fav,
        about_tower = about_tower,
        usually_tof = usually_tof,
        like_about =  like_about
    )

    formulario.save()

    return render(request, 'final.html')

    