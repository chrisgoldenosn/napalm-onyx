"""setup.py file."""
from setuptools import find_packages, setup

__author__ = 'Anas Badaha <anasb@mellanox.com'

with open("requirements.txt") as reqs_file:
    reqs = reqs_file.readlines()

setup(
    name="napalm-onyx",
    version="0.2.1",
    packages=find_packages(),
    author="Anas Badaha",
    author_email="anasb@mellanox.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation-community/napalm-onyx",
    include_package_data=True,
    install_requires=reqs,
)
