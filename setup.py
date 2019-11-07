import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()

setup(
    name="djmongoengine",
    version="1.0",
    packages=["djmongoengine"],
    description="Application to enhance performance by mongodb engine",
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
    author="Giorgi Kakulashvili",
    url="https://github.com/giorgi94/djmongoengine",
    keywords=["django", "mongodb", "graphql"],
    platforms=["OS Independent"],
    license="MIT",
    install_requires=[
        "Django>=2.0",
        "Pillow>=5.3.0",
        "mongoengine>=0.18.2",
        "pymongo>=3.9.0",
    ],
)
