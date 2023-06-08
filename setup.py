
from setuptools import find_packages, setup

#run:
#python3 setup.py sdist bdist_wheel

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='openral_py',
    version='0.5',
    description = 'Python package to work with openRAL',
    long_description='This package contains reusable components to work with openRAL in python projects. For more informations about openRAL see: https://open-ral.io/',
    author='Permarobotics GmbH',
    author_email='blech@permarobotics.com',
    url='https://github.com/AndyPermaRobotics/open-ral-python',
    packages=find_packages(include=['openral_py', 'openral_py.*']),
    license='MIT',
    install_requires=requirements,
    keywords=[
        'openRAL', 
        'regenerative agriculture', 
        'agriculture'
    ],
)