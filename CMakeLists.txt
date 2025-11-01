cmake_minimum_required(VERSION 3.16)
project(agent_weaver_core CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Compiler flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

# Source directories
include_directories(
    ${PROJECT_SOURCE_DIR}/agent_weaver_deploy/include
    ${PROJECT_SOURCE_DIR}/agent_weaver_deploy/include/agent_weaver
)

# Build configuration
option(BUILD_TESTS "Build test programs" OFF)
option(BUILD_EXAMPLES "Build example programs" ON)

# Find required packages
find_package(Threads REQUIRED)

# Library targets
add_library(agent_weaver_core_lib STATIC
    agent_weaver_deploy/src/ik_solver.cpp
    agent_weaver_deploy/src/pid_control.cpp
    agent_weaver_deploy/src/servo_driver.cpp
    agent_weaver_deploy/src/imu_fusion.cpp
    agent_weaver_deploy/src/controller.cpp
)

target_include_directories(agent_weaver_core_lib PUBLIC
    ${PROJECT_SOURCE_DIR}/agent_weaver_deploy/include
)

# Main firmware binary
add_executable(agent_weaver_firmware
    agent_weaver_deploy/src/main.cpp
)

target_link_libraries(agent_weaver_firmware
    agent_weaver_core_lib
    Threads::Threads
)

# Examples
if(BUILD_EXAMPLES)
    add_subdirectory(examples)
endif()

# Tests
if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()

# Installation
install(TARGETS agent_weaver_firmware agent_weaver_core_lib
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(DIRECTORY agent_weaver_deploy/include/
    DESTINATION include/agent_weaver
)
