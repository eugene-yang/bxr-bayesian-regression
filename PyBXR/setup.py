import os
from Cython.Build import cythonize
import numpy

os.environ["CC"] = "g++-9"
os.environ["CXX"] = "g++-9"

_BXR_compile_flags = ['-O0', '-c', '-g', '-Wno-sign-compare', '-Wno-reorder', '-DUSE_GCC']

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('PyBXR', parent_package, top_path)

    libraries = []
    if os.name == 'posix':
        libraries.append('m')

    # config.add_extension('cd_fast',
    #                      sources=['cd_fast.pyx'],
    #                      include_dirs=numpy.get_include(),
    #                      libraries=libraries)
    
    config.add_extension('PyDataFactory',
                        sources=['PyDataFactory.pyx'],
                        include_dirs=['./', '../BXRtrain/src', '../BXRClassify/src'],
                        extra_compile_args=_BXR_compile_flags)
    
    config.ext_modules = cythonize(config.ext_modules)

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())

# from distutils.core import setup
# from distutils.extension import Extension
# from Cython.Build import build_ext, cythonize

# if __name__ == "__main__":
#     setup(
#         ext_modules = cythonize([
#             Extension('PyDataFactory', sources=['PyDataFactory.pyx'],
#                       language="c++",
#                       include_dirs=['./', '../BXRtrain/src', '../BXRClassify/src'],
#                       extra_compile_args=_BXR_compile_flags),
#             # Extension('testing', sources=['testing.pyx'],
#             #           language="c++",
#             #           include_dirs=['./'])
#         ]),
#         cmdclass = { 'build_ext': build_ext }
#     )