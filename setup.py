import codecs
from setuptools import setup, find_packages

import grunt


setup(
    author='Ozan Onay',
    author_email='ozan.onay@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Topic :: Documentation'
    ],
    description=grunt.__doc__,
    entry_points={
        'console_scripts': ['grunt = grunt.render:main']
    },
    include_package_data = True,
    license='Apache',
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    name = 'grunt',
    packages = find_packages(),
    version = grunt.__version__,
)