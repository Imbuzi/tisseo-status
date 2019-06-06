#!/usr/bin/env python

from distutils.core import setup

setup(name='tisseostatus',
      version='0.0.1',
      install_requires=[
          "requests >= 2.3.0",
      ],
      description='Python interface to Tisséo\'s network and line status API',
      long_description='',
      author='Nicolas Bourasseau',
      author_email='nicolas.bourasseau@boubou.io',
      maintainer='Nicolas Bourasseau',
      author_email='nicolas.bourasseau@boubou.io',
      url='https://github.com/Imbuzi/tisseo-status',
      license='TBC',
      packages=['tisseostatus'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ]
     )
