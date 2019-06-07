all: clean build

clean:
	-@rm *.spec
	-@rm -rf build
	-@rm dist/fakevw
	@echo "Clean"

build:
	pyinstaller --clean --name fakevw -F fakevw.py

env:
	# create clean conda env for packaging
	conda create -n pyinstaller
	conda install -n pyinstaller -c conda-forge pyinstaller --yes
	@echo "############################################################"
	@echo ""
	@echo "   Run 'conda activate pyinstaller' before start packaging"
	@echo ""
	@echo "############################################################"


