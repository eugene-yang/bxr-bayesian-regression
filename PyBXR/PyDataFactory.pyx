# distutils: language = c++

# Cython wrapper around DataFactory

from libcpp cimport bool
from cython.operator import dereference

cdef extern from "DataFactory.h" namespace "DataFactory" nogil:
    cdef cppclass DataFactory:
        DataFactory(bool)
        void readFiles()
        int testing(int)

# cdef extern from "DataFactoryPython.cpp" nogil:
#     pass

cdef class PyDataFactory():
    cdef DataFactory *c_df

    def __cinit__(self):
        # pass
        self.c_df = new DataFactory(True)
    
    def tt(self, int a):
        return dereference( self.c_df ).testing( a )
    
        
        