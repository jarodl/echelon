#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test

class mytest(test):
    def run(self, *args, **kwargs):
        from runtests import runtests
        runtests()

setup(
    name='Echelon',
    version='0.1.0',
    author='DISQUS',
    author_email='opensource@disqus.com',
    url='http://github.com/disqus/echelon',
    description='A tiny cms built with Django',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
      'Django>=1.2.4',
      'South',
      'django-devserver',
      'markup',
    ],
    test_suite = 'echelon_tests',
    include_package_data=True,
    cmdclass={"test": mytest},
    classifiers=[
      'Framework :: Django',
      'Intended Audience :: Developers',
      'Intended Audience :: End Users/Desktop',
      'Operating System :: OS Independent',
      'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
