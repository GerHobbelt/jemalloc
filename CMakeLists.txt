CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(pck_prefix jemalloc)
set(pck_version $ENV{REZ_BUILD_PROJECT_VERSION})

message(STATUS "----------  Env and CMake variables-----")
message(STATUS "PROJECT_BINARY_DIR = ${PROJECT_BINARY_DIR}")
message(STATUS "env REZ_BUILD_PROJECT_VERSION = $ENV{REZ_BUILD_PROJECT_VERSION}")
message(STATUS "env REZ_BUILD_SOURCE_PATH = $ENV{REZ_BUILD_SOURCE_PATH}")
message(STATUS "env REZ_BUILD_PATH = $ENV{REZ_BUILD_PATH}")
message(STATUS "CMAKE_INSTALL_PREFIX = ${CMAKE_INSTALL_PREFIX}")
message(STATUS "----------------------------------------")

if(${REZ_BUILD_INSTALL})
   set(install_cmd make install ${make_args})
else()
   set(install_cmd "")
endif()

ExternalProject_add(
   ${pck_prefix}
   SOURCE_DIR $ENV{REZ_BUILD_SOURCE_PATH}
   BINARY_DIR $ENV{REZ_BUILD_PATH}
   PREFIX ${pck_prefix}
   UPDATE_COMMAND ""
   CONFIGURE_COMMAND $ENV{REZ_BUILD_SOURCE_PATH}/autogen.sh --prefix=${CMAKE_INSTALL_PREFIX} --with-jemalloc-prefix=__jemalloc
   BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
   INSTALL_COMMAND ${install_cmd}
   BUILD_IN_SOURCE 0
   BUILD_ALWAYS 1
)

install(
   FILES README.md
   DESTINATION cmake
)
