from d3_primeri.services.services import PrikazatiServis
from pkg_resources import resource_string

class SlozenPrikaz(PrikazatiServis):

    def naziv(self):
        return "Slozen prikaz"

    def identifier(self):
        return "ExPreSiVeNessSlozenPrikaz"

    def prikazati(self):
        return resource_string('slozen_prikaz.prikaz', 'show.html')