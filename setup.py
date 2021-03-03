# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='sentiment-analysis',
    version='0.0.1',
    description='Sentiment analysis for the german language',
    long_description=readme,
    author='Christoph Koenning',
    author_email='chris@casualcompany.de',
    url='https://github.com/Covidioten/BAPraktikumSentimentAnalyse',
    packages=find_packages(exclude=('tests', 'docs'))
)
