# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='venn',
      version='0.1',
      description='Venn diagram sections and plots for arbitrary nuber of sets and max. 5 sets, respectively.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Public Domain',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Visualization',
      ],
      url='',
      author='kp14',
      author_email='',
      license='Public Domain',
      packages=['venn'],
      install_requires=[ 'jinja2' ],
      include_package_data=True)