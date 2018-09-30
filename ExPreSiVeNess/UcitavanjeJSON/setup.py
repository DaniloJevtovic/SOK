from setuptools import setup, find_packages

setup(
    name="prodavnica-ucitavanje-json",
    version="0.1",
    packages=find_packages(),
    package_data={
        '' : ['sample.json']
    },
    install_requires=['d3-primeri>=0.1'],
    entry_points = {
        'ExPreSiVeNess.ucitati':
            ['ucitavanje_file_json=ucitavanje_json.json.ucitavanje_json_file:UcitatiProdavniceJson'],
    },
    zip_safe=False
)