# distutils: language = c++
# Cython wrapper around DataFactory

from libcpp cimport string
from cython.operator import dereference


cdef extern from "DataFactory.h" nogil:
    cdef cppclass DataFactory:
        # DataFactory(bool)
        DataFactory()
        # void readFiles()
        int testing(int)
        # void MakeSparseMatrix(string)
        # void ttt()
        # int ttt


cdef class PyDataFactory:
    cdef DataFactory *c_df

    def __cinit__(self):
        # pass
        self.c_df = new DataFactory()
    
    def tt(self, int a):
        # return a
        # dereference( self.c_df ).readFiles()
        # return dereference( self.c_df ).testing(a)
        # self.c_df.MakeSparseMatrix("123".encode())
        return self.c_df.testing(a)
    
        
        