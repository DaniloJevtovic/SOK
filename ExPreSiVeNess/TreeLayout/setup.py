from setuptools import setup, find_packages

setup(
    name="ExPreSiVeNess-TreeLayoutPrikaz",
    version="0.1",
    packages=find_packages(),
    install_requires=['d3-primeri>=0.1'],
    entry_points = {
        'ExPreSiVeNess.prikazati':
            ['tree=tree_layout.tree_layout_prikaz.tree:TreeLayoutPrikaz'],
    },
    zip_safe=False
)