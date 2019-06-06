PY=python3

all: clean build

clean:
	-@rm -rf build/
	-@rm *.so *.cxx *_wrap.py
	@echo "Cleaned"

build: swig pysetup
	
swig:
	swig -c++ -python -py3 *.i

pysetup:
	$(PY) setup.py build_ext -i
