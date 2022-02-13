cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(PythonLibs REQUIRED)
include_directories("${PYTHON_INCLUDE_DIR}")
add_definitions(
  -DPYTHONQT_USE_RELEASE_PYTHON_FALLBACK
  -DPYTHONQT_SUPPORT_NAME_PROPERTY
  )

find_package (Qt6 COMPONENTS Core REQUIRED)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
message ("Qt6Dir => ${Qt6_DIR}")
add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS} Qt6::Core)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
