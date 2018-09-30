import xml.etree.cElementTree as ET
from d3_primeri.models import Element, Attribute, Link
from d3_primeri.services.services import UcitatiServis
from pkg_resources import resource_string

sample = resource_string('ucitavanje_xml.xml','sample.xml')
root=ET.fromstring(sample)
#root=tree.getroot()

class UcitatiProdavniceXml(UcitatiServis):

    def naziv(self):
        return "Xml plugin"

    def identifier(self):
        return "ucitati_prodavnice_xml"

    def ucitati(self):

        Link.objects.all().delete()
        Attribute.objects.all().delete()
        Element.objects.all().delete()
        self.ucitaj_cvor(root)


    def ucitaj_cvor(self, cvor):
        element = Element(name=cvor.tag)
        element.save()

        for name, value in cvor.attrib.items():
            attribute = Attribute(name=name, value=value, parent=element)
            attribute.save()

        for child in cvor:
            child_element = self.ucitaj_cvor(child)
            link=Link(source = element,target = child_element, name = 'sadrzi')
            link.save()

        return element

