from setuptools import setup, find_packages

setup(
    name="prodavnica-ucitavanje-xml",
    version="0.1",
    packages=find_packages(),
    package_data={
        '' : ['sample.xml']
    },
    install_requires=['d3-primeri>=0.1'],
    entry_points = {
        'ExPreSiVeNess.ucitati':
            ['ucitavanje_file_xml=ucitavanje_xml.xml.ucitavanje_xml_file:UcitatiProdavniceXml'],
    },
    zip_safe=False
)