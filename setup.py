# import sys
import io
import os
import re
from setuptools import setup, find_packages
# from os import path, makedirs
# from shutil import copytree

#############################################################
# Get version
#############################################################


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


current_version = find_version("genomkit", "__init__.py")


#############################################################
# Setup function
#############################################################

with open("README.md", "r") as fh:
    long_description = fh.read()

short_description = 'genomkit'

setup(
    name='genomkit',
    version=current_version,
    author='Chao-Chung Kuo',
    author_email='chao-chung.kuo@rwth-aachen.de',
    description=short_description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chaochungkuo/genomkit',
    packages=find_packages(),
    install_requires=[
        'Click', "numpy==1.26.4", "pysam==0.22.0"
    ],
    # entry_points={
    #     'console_scripts': [
    #         'gpm=gpm.main:main',
    #     ],
    # },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
