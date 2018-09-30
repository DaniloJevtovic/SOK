from d3_primeri.models import Element, Link, Attribute
from d3_primeri.services.services import UcitatiService


class UcitatiPodatkeKod(UcitatiService):
    def naziv(self):
        return "Ucitati podatke iz koda"
    def identifier(self):
        return "ucitati_podatke_kod"

    def ucitati(self):
        self._ubaci_elemente()
        self._ubaci_atribute()
        self._ubaci_linkove()

    def _ubaci_elemente(self):
        Element.objects.all().delete()

        e0 =Element(name="Cvor", text="glavni cvor")
        e0.save()

        e1=Element(name="Element1", text="text1")
        e1.save()

        e2 = Element(name="Element2", text="text2")
        e2.save()

        e3 = Element(name="Element3", text="text3")
        e3.save()

        e4 = Element(name="Element4")
        e4.save()

        e5 = Element(name="Element5")
        e5.save()

        e6 = Element(name="Element6")
        e6.save()

        ea = Element(name="Element A", text="elementA")
        ea.save()

        eb = Element(name="Element B", text="element b")
        eb.save()



    def _ubaci_atribute(self):
        Attribute.objects.all().delete()

        a1 = Attribute(name="atribut1", value="v1")
        a1.parent = Element.objects.get(name="Element1")
        a1.save()

        a2 = Attribute(name="atribut2", value="v2")
        a2.parent = Element.objects.get(name="Element1")
        a2.save()

        a3 = Attribute(name="atribut3", value="v3")
        a3.parent = Element.objects.get(name="Element2")
        a3.save()

        a4 = Attribute(name="atribut4", value="v4")
        a4.parent = Element.objects.get(name="Element4")
        a4.save()

        aa = Attribute(name="atribut aa", value="aa")
        aa.parent = Element.objects.get(name="Element A")
        aa.save()

        ab = Attribute(name="atribut ab", value="ab")
        ab.parent = Element.objects.get(name="Element B")
        ab.save()




    def _ubaci_linkove(self):
        Link.objects.all().delete()

        l0 = Link(name="sadrzi")
        l0.source = Element.objects.get(name="Cvor")
        l0.target = Element.objects.get(name="Element1")
        l0.save()

        l1 = Link(name = 'sadrzi')
        l1.source = Element.objects.get(name="Element1")
        l1.target = Element.objects.get(name="Element2")
        l1.save()

        l1 = Link(name='sadrzi2')
        l1.source = Element.objects.get(name="Element1")
        l1.target = Element.objects.get(name="Element3")
        l1.save()

        l1 = Link(name='sadrzi2')
        l1.source = Element.objects.get(name="Element3")
        l1.target = Element.objects.get(name="Element5")
        l1.save()

        l1 = Link(name='sadrzi3')
        l1.source = Element.objects.get(name="Element4")
        l1.target = Element.objects.get(name="Element6")
        l1.save()

        l1 = Link(name='sadrzi2')
        l1.source = Element.objects.get(name="Element1")
        l1.target = Element.objects.get(name="Element4")
        l1.save()

        la = Link(name="sadrzi")
        la.source = Element.objects.get(name="Cvor")
        la.target = Element.objects.get(name="Element A")
        la.save()

        lb = Link(name="sadrzi")
        lb.source = Element.objects.get(name="Cvor")
        lb.target = Element.objects.get(name="Element B")
        lb.save()

