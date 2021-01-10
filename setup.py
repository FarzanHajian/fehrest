import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'LICENSE')) as f:
    LICENSE = f.read()

requires = [
    'pelican[markdown]',
    'python-slugify'
]

setup(
    name='fehrest',
    version='0.1',
    description='A static site generator for your files',
    long_description=README,
    author='Farzan Hajian',
    author_email='farzan.hajian@gmail.com',
    url='',
    keywords='',
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'fehrest = fehrest:main',
        ],
    },
)
