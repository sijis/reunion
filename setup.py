#!/usr/bin/env python3
"""Installer"""

from setuptools import find_packages, setup

with open('requirements.txt', 'rt') as reqs_file:
    REQUIREMENTS = reqs_file.readlines()

setup(
    name='reunion',
    description='Library to capture meetings in chat.',
    long_description=open('README.rst').read(),
    author='Sijis Aviles',
    author_email='sijis.aviles+github@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    setup_requires=['setuptools_scm'],
    use_scm_version={'local_scheme': 'dirty-tag'},
    install_requires=REQUIREMENTS,
    include_package_data=True,
    keywords='meetings chat meetbot',
    url='https://github.com/saviles/reunion',
    download_url='https://github.com/saviles/reunion',
    platforms=['OS Independent'],
    license='Apache License (2.0)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
