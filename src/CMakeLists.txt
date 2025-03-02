find_package(SWIG 4.3 COMPONENTS python)
include(UseSWIG)

find_package(Python3 COMPONENTS Interpreter Development)

install(FILES "${CMAKE_CURRENT_LIST_DIR}/py.typed" DESTINATION .)

add_subdirectory(example)

set(CPACK_INCLUDE_TOPLEVEL_DIRECTORY OFF)
set(CPACK_OUTPUT_FILE_PREFIX "")
set(CPACK_GENERATOR "ZIP" CACHE STRING "Only a .zip package will be created.")
include(CPack)
