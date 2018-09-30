from django.apps.registry import apps
from django.shortcuts import render, redirect


def index(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    plugini1 = apps.get_app_config('d3_primeri').plugini_prikaz
    return render(request,"index.html",{"title":"Index","plugini_ucitavanje":plugini, "plugini_prikazivanje":plugini1})

def ucitavanje_plugin(request,id):
    request.session['izabran_plugin_ucitavanje']=id
    plugini=apps.get_app_config('d3_primeri').plugini_ucitavanje
    for i in plugini:
        if i.identifier() == id:
            i.ucitati()
    return redirect('index')

def prikazivanje_plugin(request,id):
    request.session['izabran_plugin_prikazivanje']=id
    plugini=apps.get_app_config('d3_primeri').plugini_prikazivanje
    for i in plugini:
        if i.identifier() == id:
            return i.prikazati(request)

def primer1(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request,"primer1.html",{"title":"Primer1","plugini_ucitavanje":plugini})


def primer2(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer2.html", {"title": "Primer2","plugini_ucitavanje":plugini})


def primer3(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer3.html", {"title": "Primer3","plugini_ucitavanje":plugini})

def primer4(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer4.html", {"title": "Primer4","plugini_ucitavanje":plugini})


def primerPanZoom(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    plugini1 = apps.get_app_config('d3_primeri').plugini_prikazivanje
    return render(request, "primerPanZoom.html", {"title": "Primer Pan Zoom","plugini_ucitavanje":plugini,
                                                  "plugini_prikazivanje": plugini1})

def sok_view(request):
    return render(request, "sok.html")