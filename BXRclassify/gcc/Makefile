# CC=g++-9
# CFLAG=-DUSE_GCC -g -I/home/lshenzhi/BXRclassify/src/tclap-1.0.5/include 

# all: BXRclassify
# BXRclassify: MultiModel.o BXRclassify.o parseModelFiles.o readLabelFile.o readTestVectorFile.o genResultFile.o
# 	$(CC) $(CFLAG) -static -o BXRclassify MultiModel.o BXRclassify.o parseModelFiles.o  readLabelFile.o readTestVectorFile.o genResultFile.o
# 	cp BXRclassify ../src/

# BXRclassify.o: ../src/BXRclassify.cpp
# 	$(CC) $(CFLAG) -c $<

# MultiModel.o: ../src/MultiModel.cpp ../src/MultiModel.h 
# 	$(CC) $(CFLAG) -c ../src/MultiModel.cpp -o MultiModel.o 

# parseModelFiles.o: ../src/parseModelFiles.cpp ../src/MultiModel.h
# 	$(CC) $(CFLAG) -c ../src/parseModelFiles.cpp -o parseModelFiles.o

# readLabelFile.o: ../src/readLabelFile.cpp ../src/MultiModel.h
# 	$(CC) $(CFLAG) -c ../src/readLabelFile.cpp -o readLabelFile.o

# readTestVectorFile.o: ../src/readTestVectorFile.cpp ../src/MultiModel.h
# 	$(CC) $(CFLAG) -c ../src/readTestVectorFile.cpp -o readTestVectorFile.o

# genResultFile.o: ../src/genResultFile.cpp ../src/MultiModel.h
# 	$(CC) $(CFLAG) -c ../src/genResultFile.cpp -o genResultFile.o


# clean:
# 	rm *.o BXRclassify ../src/BXRclassify


CC=g++-9
CFLAGS=-O0 -c -g -std=c++11 -Wno-deprecated -I../src/tclap-1.0.5/include -I../src -DUSE_GCC -DSYMBOLIC
LDFLAGS=-G
# SOURCES=DataFactory.cpp Matrix.cpp StrataSplit.cpp Milliseconds.cpp OutputFormat.cpp Likelihood.cpp PolyZO.cpp QNOpt.cpp CommandLine.cpp
OBJECTS=BXRclassify.o MultiModel.o parseModelFiles.o readLabelFile.o readTestVectorFile.o genResultFile.o

EXECUTABLE=BXRclassify

all: $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS)
	# for mac, no static build
	$(CC) $(OBJECTS) -o $@	
	# $(CC) -static $(OBJECTS) -o $@

%.o: ../src/%.cpp
	$(CC) $(CFLAGS) $< 

clean:
	-rm *.o BXRclassify
