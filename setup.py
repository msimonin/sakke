# coding: utf8
from setuptools import setup, find_packages
from sakke import __version__

setup(
    name='sakke',
    version=__version__,
    license='GPL-3.0',
    author='Matthieu Simonin',
    author_email='matthieu.simonin@gmail.com',
    url='https://github.com/msimonin/sakke',
    description='SaKKe est un utilitaire simple de génération de statistiques personnalisées de devoirs.',
    packages=find_packages(),
    package_data = {'': ['templates/stats.tex.j2', 'templates/stats.html.j2']},
    install_requires=[
        'docopt==0.6.2',
        'Jinja2',
        'pandas~=1.2',
        'odfpy~=1.4',
        'seaborn~=0.11'
    ],
    entry_points={'console_scripts': ['sakke = sakke.sakke:main']}
)
