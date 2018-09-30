from d3_primeri.services.services import PrikazatiServis
from pkg_resources import resource_string

class TreeLayoutPrikaz(PrikazatiServis):

    def naziv(self):
        return "TreeLayout prikaz"

    def identifier(self):
        return "ExPreSiVeNessTreeLayoutPrikaz"

    def prikazati(self):
        return resource_string('tree_layout.tree_layout_prikaz', 'tree.html')