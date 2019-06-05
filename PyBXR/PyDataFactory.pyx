# distutils: language = c++
# Cython wrapper around DataFactory

from libcpp cimport bool
from cython.operator import dereference

cdef extern from "DataFactory.cpp" namespace "DD" nogil:
    cdef cppclass DataFactory:
        DataFactory()
        int testing()

# cdef extern from "DataFactory.h" nogil:
#     cdef cppclass DataFactory:
#         # DataFactory(bool)
#         # DataFactory()
#         # void readFiles()
#         int testing()
#         # int ttt



# cdef extern from "../BXRtrain/src/DataFactory.cpp" nogil:
#     pass

cdef class PyDataFactory:
    cdef DataFactory *c_df

    def __cinit__(self):
        # pass
        self.c_df = new DataFactory()
    
    def tt(self, int a):
        # return a
        return dereference( self.c_df ).testing()
    
        
        