#!/usr/bin/env python3

import pkg_resources
import pathlib
import setuptools

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setuptools.setup(
    name="COOKIEDUMPER",
    version="0.0.1r.0", # first release
    author="iiTsLhaj",
    description="Simple Cookies dumper used for hoyolab daily check in",
    python_requires='>=3.6',
    install_requires=install_requires,
    url="https://github.com/iTsLhaj/HLCookieDumper"
)