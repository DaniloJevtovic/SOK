from setuptools import setup, find_packages

setup(
    name="ExPreSiVeNess-SlozenPrikaz",
    version="0.1",
    packages=find_packages(),
    install_requires=['d3-primeri>=0.1'],
    entry_points = {
        'ExPreSiVeNess.prikazati':
            ['show=slozen_prikaz.prikaz.show:SlozenPrikaz'],
    },
    zip_safe=False
)