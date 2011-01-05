all: clean build test

clean:
	python setup.py clean

build:
	python setup.py build_ext --inplace

install:
	python setup.py install

test:
	python pqtree_test.py
