from setuptools import setup, find_packages

setup(
    name="ExPreSiVeNess-JednostavanPrikaz",
    version="0.1",
    packages=find_packages(),
    install_requires=['d3-primeri>=0.1'],
    entry_points = {
        'ExPreSiVeNess.prikazati':
            ['jednostavan=jednostavan_prikaz1.jednostavan1.jednostavan:JednostavanPrikaz1'],
    },
    zip_safe=False
)