add_library(example SHARED example.c)
target_include_directories(example PUBLIC ${CMAKE_CURRENT_LIST_DIR})

swig_add_library(py_example TYPE SHARED LANGUAGE python SOURCES example.i)
target_link_libraries(py_example PRIVATE example)
target_include_directories(py_example PRIVATE "${Python3_INCLUDE_DIRS}")

install(TARGETS example py_example LIBRARY DESTINATION example)
install(FILES
  "${CMAKE_CURRENT_BINARY_DIR}/example.py"
  "${CMAKE_CURRENT_LIST_DIR}/example.pyi"
  "${CMAKE_CURRENT_LIST_DIR}/hl_example.py"
  DESTINATION example)

