import os
import numpy

from pathlib import Path

os.environ["CC"] = "g++-9"
os.environ["CXX"] = "g++-9"

_BXR_compile_flags = ['-O0', '-c', '-Wall', '-g', '-Wno-sign-compare', '-Wno-reorder', '-DUSE_GCC']

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import build_ext, cythonize

if __name__ == "__main__":
    setup(
        ext_modules = [
            Extension('DataFactory', 
                      sources=['DataFactory_wrap.cxx', 
                            #    '../BXRtrain/src/DataFactory.h', 
                               '../BXRtrain/src/DataFactory.cpp'],
                      language="c++",
                      include_dirs=['./'],
                      extra_compile_args=_BXR_compile_flags),
            # Extension('testing', sources=['testing.pyx'],
            #           language="c++",
            #           include_dirs=['./'])
        ],
        cmdclass = { 'build_ext': build_ext }
    )