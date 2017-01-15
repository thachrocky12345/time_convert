from setuptools import find_packages, setup

setup(
    name='time_convert',
    version='1.0.0',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'': ['']},
    install_requires=[

        ''
    ],
    description='Python library containing time convert'
)
