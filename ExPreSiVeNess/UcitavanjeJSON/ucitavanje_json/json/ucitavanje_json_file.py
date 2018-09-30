from d3_primeri.models import Prodavnica, Kategorija, Artikal

from d3_primeri.services.services import UcitatiServis
from d3_primeri.models import Element,Attribute,Link
import  json
from pkg_resources import resource_string

sample = resource_string('ucitavanje_json.json','sample.json')
d=json.loads(sample)

class UcitatiProdavniceJson(UcitatiServis):

    def jeste_element(self, element):
        tip = type(element)
        return  tip is dict or tip is list

    def jeste_atribut(self, element):
        tip = type(element)
        return tip is str or\
               tip is int or \
               tip is float or \
               tip is bool or \
               tip is None

    def formiraj_element(self, naziv):
        element = Element(name=naziv)
        element.save()
        return element

    def formiraj_atribut(self, naziv, vrednost, element):
        atribut = Attribute(name=naziv, value=vrednost, parent=element)
        atribut.save()
        return atribut

    def formiraj_vezu(self, roditelj, dete, ime):
        veza = Link(name=ime, source=roditelj, target=dete)
        veza.save()
        return veza

    def vrednost_atributa(self, atribut):
        if atribut is None:
            return ""
        return str(atribut)

    def naziv(self):
        return "Ucitati prodavnice iz json fajla"

    def identifier(self):
        return "ucitati_prodavnice_json"

    def ucitati(self):
        Link.objects.all().delete()
        Attribute.objects.all().delete()
        Element.objects.all().delete()
        self.ucitaj_model(d)

    def ucitaj_model(self, koren):
        korenski_element = self.formiraj_element("json_root")
        if self.jeste_atribut(koren):
            self.formiraj_atribut("atribut", self.vrednost_atributa(koren), korenski_element)

        if self.jeste_element(koren):
            self.ucitaj_cvor('json_root', koren)
        else:
            raise AssertionError('Nepoznat tip ' + str(type(koren)))


    def ucitaj_cvor(self, naziv,  cvor):
        cvorni_element = self.formiraj_element(naziv)
        if type(cvor) is dict:
            for k, v in cvor.items():
                if self.jeste_atribut(v):
                    self.formiraj_atribut(k, v, cvorni_element)
                elif self.jeste_element(v):
                    self.formiraj_vezu( cvorni_element, self.ucitaj_cvor(k, v), "sadrzi" )
                else:
                    raise AssertionError('Nepoznat tip ' + str(type(v)))
        elif type(cvor) is list:
            for i, v in enumerate(cvor):
                if self.jeste_atribut(v):
                    self.formiraj_atribut(str(i), v, cvorni_element)
                elif self.jeste_element(v):
                    self.formiraj_vezu(cvorni_element, self.ucitaj_cvor(str(i), v), "sadrzi")
                else:
                    raise AssertionError('Nepoznat tip ' + str(type(v)))
        else:
            raise AssertionError('Nepoznat tip ' + str(type(cvor)))
        return cvorni_element
