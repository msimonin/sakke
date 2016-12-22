from setuptools import setup, find_packages
from qs import __version__

setup(
    name='qs',
    version=__version__,
    license='GPL-3.0',
    packages=find_packages(),
    install_requires=[
        'Jinja2==2.8',
    ],
    entry_points={'console_scripts': ['qs = qs.qs:main']}
)
