PYTHON=python3

all: clean build test

cl: clean

clean:
	@rm -rf build
	@rm -f *.c *.cpp *.so
	@echo "Cleaned"

build:
	@$(PYTHON) setup.py build_ext -i

test:
	@echo "==== TESTING ===="
	@$(PYTHON) test.py
