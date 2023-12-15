from sequence import __version__

from setuptools import setup, find_packages, find_namespace_packages

setup(
  name='sequentium',
  version=f'{__version__}',
  license='MIT',
  author='Vasco Schiavo',
  author_email='vasco.schiavo@protonmail.com',
  url='https://github.com/VascoSch92',
  description='A package to work with sequences',
  packages=find_namespace_packages(exclude=['tests']),
  entry_points={
        'console_scripts': ['sequence=sequence:main']
    },
  download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords=['MATH'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Users',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)

