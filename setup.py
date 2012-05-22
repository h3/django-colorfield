# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-colorfield',
    version='1.0.0',
    description='Simple colorfield for django (optimized for grappelli)',
    author='Maxime Haineault (Motion Média)',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/django-colorfield',
    download_url='https://h3@github.com/h3/django-colorfield.git',
    packages=find_packages(),
    include_package_data=True,
#   package_data={'colorfield': [
#       'templates/*',
#       ]},
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)

