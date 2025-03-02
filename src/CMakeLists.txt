find_package(SWIG 4.3 COMPONENTS python)
include(UseSWIG)

find_package(Python3 COMPONENTS Interpreter Development)

add_library(example SHARED example.c)
target_include_directories(example PUBLIC ${CMAKE_CURRENT_LIST_DIR})

swig_add_library(py_example TYPE SHARED LANGUAGE python SOURCES example.i)
target_link_libraries(py_example PRIVATE example)
target_include_directories(py_example PRIVATE "${Python3_INCLUDE_DIRS}")

install(TARGETS example py_example LIBRARY DESTINATION .)
install(FILES
  "${CMAKE_CURRENT_BINARY_DIR}/example.py"
  "${CMAKE_CURRENT_LIST_DIR}/py.typed"
  "${CMAKE_CURRENT_LIST_DIR}/example.pyi"
  DESTINATION .)

set(CPACK_INCLUDE_TOPLEVEL_DIRECTORY OFF)
set(CPACK_OUTPUT_FILE_PREFIX "")
set(CPACK_GENERATOR "ZIP" CACHE STRING "Only a .zip package will be created.")
include(CPack)
