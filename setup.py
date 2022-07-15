#!/usr/bin/env python

import os
from setuptools import setup

SETUP_DIR = os.path.dirname(__file__)

long_description = ""

with open("README.pypi.rst") as readmeFile:
    long_description = readmeFile.read()

setup(
    name="arvados-tes",
    version="1.0",
    description="GA4GH Task Execution Service implementation for Arvados",
    long_description=long_description,
    author="Peter Amstutz",
    author_email="peter.amstutz@curii.com",
#    url="https://github.com/common-workflow-language/cwltool-service",
#    download_url="https://github.com/common-workflow-language/cwltool-service",
    license="Apache 2.0",
    python_requires="~=3.7",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    packages=["arvados_tes"],
    package_data={"arvados_tes": ["openapi/task_execution_service.openapi.yaml"]},
    include_package_data=True,
    install_requires=[
        "connexion",
        "arvados-python-client",
        "tornado",
    ],
    entry_points={
        "console_scripts": [
            "arvados-tes=arvados_tes.main:main",
        ]
    },
    extras_require={
    },
    zip_safe=False,
    platforms=["MacOS X", "Posix"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
