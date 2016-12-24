from setuptools import setup, find_packages
from sakke import __version__

setup(
    name='sakke',
    version=__version__,
    license='GPL-3.0',
    author='Matthieu Simonin',
    author_email='matthieu.simonin@gmail.com',
    url='https://github.com/msimonin/sakke',
    packages=find_packages(),
    package_data = {'': ['templates/stats.tex.j2']},
    install_requires=[
        'docopt==0.6.2',
        'Jinja2==2.8',
        'numpy==1.11.3'
    ],
    entry_points={'console_scripts': ['sakke = sakke.sakke:main']}
)
