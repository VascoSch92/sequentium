from distutils.core import setup
from sequence import __version__

setup(
  name='sequentium',
  packages=['sequentium'],
  version=f'{__version__}',
  license='MIT',
  description='A package to work with sequences',
  author='Vasco Schiavo',
  author_email='vasco.schiavo@protonmail.com',
  url='https://github.com/VascoSch92',
  download_url='https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
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
