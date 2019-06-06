/*
Implementing the connector that takes in the variable natively from Python. 
Just an interface to put things in. 

Author: Eugene Yang < eugene2528 at gmail dot com >
*/

#include "DataFactory.h"
#include "Data.h"
#include "logging.h"
// #include "OutputFormat.cpp"
// #include "Matrix.cpp"
// #include "Likelihood.cpp"
#include "DataFactory.cpp"
#include "vector"

DataFactory::DataFactory() {
    // Set everything directly from Cython
}

int DataFactory::testing(int a) {
    // ttt();
    // readFiles();
    return a+10;
}


// RowSetIterator* MemRowSet::iterator() {
// 	return new MemRowSetIterator(*this);
// }


// RowSetIterator* PlainYRowSet::iterator() {
// 	return new PlainYRowSetIterator(*this);
// }

// PlainYRowSetIterator* PlainYRowSet::plainYiterator() {
// 	// return new PlainYRowSetIterator(*this);
// }