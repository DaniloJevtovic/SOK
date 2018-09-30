import pkg_resources
from django.apps import AppConfig


class D3PrimeriConfig(AppConfig):
    name = 'd3_primeri'
    plugini_ucitavanje=[]
    #plugini_prikazivanje=[]

    plugini_prikaz=[]

    def ready(self):
        #self.plugini_ucitavanje=load_plugins("prodavnica.ucitati")
        #self.plugini_prikazivanje=load_plugins("prodavnica.prikazati")

        self.plugini_ucitavanje=load_plugins("ExPreSiVeNess.ucitati")
        self.plugini_prikaz=load_plugins("ExPreSiVeNess.prikazati")



def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins
