from d3_primeri.services.services import PrikazatiServis
from pkg_resources import resource_string

class JednostavanPrikaz1(PrikazatiServis):

    def naziv(self):
        return "Jednostavan prikaz"

    def identifier(self):
        return "ExPreSiVeNessJednostavanPrikaz"

    def prikazati(self):
        return resource_string('jednostavan_prikaz1.jednostavan1', 'jednostavan.html')