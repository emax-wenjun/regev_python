from distutils.core import setup
import numpy


setup(name='regev_python',
      description='A python implementation of the packed Regev encryption scheme',
      author='Jesko Dujmovic',
      version='0.1',
      include_dirs=[numpy.get_include()])
