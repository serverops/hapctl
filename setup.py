# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '1.0'

setup(name='haproxy',
      version=__version__,
      description="Communicating with the HAProxy Control Socket",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX",
          "Environment :: Console",
          "Programming Language :: Python",
          "Topic :: Internet",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='haproxy',
      author='Chris Fidao',
      author_email='chris@serverops.io',
      url='https://github.com/serverops/python-haproxy',
      license='MIT',
      package_dir={'': 'lib'},
      packages=find_packages('lib'),
      install_requires=['click'],
      entry_points='''
          [console_scripts]
          hapctl=haproxy.cmd.hapctl:cli
      '''
)
