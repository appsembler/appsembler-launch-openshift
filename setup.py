import os
from setuptools import setup, find_packages

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

setup(name='Appsembler Launch',
      version='0.1',
      description='Appsembler launch widget for open source applications',
      author='Nate Aune & Filip Jukic',
      author_email='support@appsembler.com',
      url='https://github.com/appsembler/appsembler-launch',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[],
      )
