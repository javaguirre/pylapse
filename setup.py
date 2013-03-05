import os
from distutils.core import setup


setup(
    name='PyLapse',
    version='0.1.0',
    author='Javier Aguirre',
    author_email='contacto@javaguirre.net',
    packages=['pylapse'],
    scripts=['bin/pylapse_menu.py'],
    url='http://pypi.python.org/pypi/PyLapse/',
    license='LICENSE.txt',
    description='A simple application to build timelapses using a webcam, V4l2 and ImageMagick',
    long_description=open('README.txt').read(),
    install_requires=['PIL == 1.1.7',
                      'v4l2 == 0.2',
                      'v4l2capture == 1.4']
)
