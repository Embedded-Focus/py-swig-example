all: build/_CPack_Packages/Linux/ZIP/py-swig-example-0.1.0-Linux.zip

build:
	mkdir -p build

build/src/_py_example.so: CMakeLists.txt \
	src/CMakeLists.txt \
	src/example/example.c \
	src/example/example.h \
	src/example/example.i | build
	cmake -S . -Bbuild -DCMAKE_BUILD_TYPE=Debug -GNinja
	bear -- cmake --build build

build/_CPack_Packages/Linux/ZIP/py-swig-example-0.1.0-Linux.zip: build/src/_py_example.so | build
	cmake --build build --target package -v

.PHONY: test
test: build/_CPack_Packages/Linux/ZIP/py-swig-example-0.1.0-Linux.zip
	pytest -svv

.PHONY: clean
clean:
	rm -rf build
