from distutils.core import setup
from setuptools import find_packages

setup(
	name='Fuzzython',
	version='0.1.0',
	author='Medialab-UH',
	author_email='yudy@uh.cu',
	packages= find_packages(),
	url='https://github.com/yudivian/fuzzython',
	license='LICENSE.txt',
	description='Fuzzy Logic and Fuzzy Inference Python 3 Library',
	long_description=open('README.md').read(),
	keywords='Fuzzy Logic Library',
) 
