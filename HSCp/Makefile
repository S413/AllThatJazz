comp=g++

comp_flags=-O3 -Wall -shared -std=c++17 -fPIC

include_dirs=-I/usr/include/pybind11/ \
	     -I/usr/include/python3.8/ \
	     -I./

defaults:
	${comp} ${comp_flags} $$(python3 -m pybind --includes) HS.cpp -o HSCp$$(python3-config --extension-suffix) ${include_dirs}

test:
	python3 -m pytest testIni.py
	python3 -m pytest testObjectFun.py
	python3 -m pytest testHSA.py

clean:
	rm -rf *.so __pycache__
