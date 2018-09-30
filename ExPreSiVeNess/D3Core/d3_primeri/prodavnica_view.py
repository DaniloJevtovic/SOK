from d3_primeri.models import Element, Attribute, Link
from django.apps.registry import apps
from django.shortcuts import render


def force_layout_slozen(self, request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    plugini1 = apps.get_app_config('d3_primeri').plugini_prikaz
    elementi = Element.objects.all()
    atributi = Attribute.objects.all()
    linkovi = Link.objects.all()

    return render(request, "forceSlozenPrikaz.html",
                  {"title": "Slozen prikaz prikaz",
                   "plugini_ucitavanje": plugini,
                   "plugini_prikazivanje": plugini1,
                   "elementi": elementi,
                   "atributi": atributi,
                   "linkovi": linkovi})


def prikazati(self, request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    plugini1 = apps.get_app_config('d3_primeri').plugini_prikaz
    elementi = Element.objects.all()
    atributi = Attribute.objects.all()
    linkovi = Link.objects.all()

    return render(request, "jednostavanPrikaz.html",
                  {"title": "Jednostavan prikaz",
                   "plugini_ucitavanje": plugini,
                   "plugini_prikazivanje": plugini1,
                   "elementi": elementi,
                   "atributi": atributi,
                   "linkovi": linkovi})
