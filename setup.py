from setuptools import setup, find_packages
import os

setup(
    name='medialog.xdvsubskins',
    version='0.1',
    description='An installable Diazo theme for Plone 4.1',
    long_description=open("README.rst", "rb").read() +
                     open(os.path.join("docs", "HISTORY.txt"), "rb").read(),
    author='Espen Moe-Nilssen',
    author_email='espen@medialog.no',
    url='http://products.medialog.no',
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
    ],
    keywords='web zope plone theme medialog subskins diazo',
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=[
        'medialog',
    ],
    install_requires=[
        'setuptools',
        'plone.app.theming',
        'medialog.subskins'
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
)
