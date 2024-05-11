cmake_minimum_required(VERSION 3.10)
project("main" VERSION 1.0.0) # Adjust the project name as necessary

# Set the C++ standard to use
set(CMAKE_CXX_STANDARD 17)

# Our main project will be an executable with the main.cpp in the same folder as this file.
add_executable(${PROJECT_NAME} main.cpp)    # Adjust the name of .cpp file as necessary

# Set this as the startup project if we're using Visual Studio
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ${PROJECT_NAME})

# Define the path to the SGCore source directory
set(SENSEGLOVE_SOURCE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/SenseGlove-API-master)  # Adjust the relative path as necessary

# Add the include directory for header files
include_directories("${SENSEGLOVE_SOURCE_PATH}/include")     # Adjust the relative path as necessary

# Determine path to binaries based on platform
if(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set(SGCONNECT_BINS "${SENSEGLOVE_SOURCE_PATH}/lib/linux")   # Adjust the relative path as necessary
    set(SGCORE_BINS "${SENSEGLOVE_SOURCE_PATH}/lib/linux")   # Adjust the relative path as necessary
else()
    set(SGCONNECT_BINS "${SENSEGLOVE_SOURCE_PATH}/lib/win64/msvc143")   # Adjust the relative path as necessary
    set(SGCORE_BINS "${SENSEGLOVE_SOURCE_PATH}/lib/win64/msvc143")   # Adjust the relative path as necessary
endif()

# Find and link the Debug and Release binaries for SGConnect and SGCore
find_library(SGCONNECT_BIN_DEBUG NAMES sgconnect HINTS ${SGCONNECT_BINS}/debug)
find_library(SGCONNECT_BIN_RELEASE NAMES sgconnect HINTS ${SGCONNECT_BINS}/release)
find_library(SGCORE_BIN_DEBUG NAMES sgcore HINTS ${SGCORE_BINS}/debug)
find_library(SGCORE_BIN_RELEASE NAMES sgcore HINTS ${SGCORE_BINS}/release)

# Link the appropriate binaries based on configuration
target_link_libraries(${PROJECT_NAME}
    debug ${SGCONNECT_BIN_DEBUG} ${SGCORE_BIN_DEBUG}
    optimized ${SGCONNECT_BIN_DEBUG} ${SGCORE_BIN_DEBUG})

# Copy the .dll files to the output directory after building (for Windows)
if(NOT ${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    add_custom_command(
        TARGET ${PROJECT_NAME}
        POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy "${SGCONNECT_BINS}/$<CONFIGURATION>/sgconnect.dll" "$<TARGET_FILE_DIR:${PROJECT_NAME}>"
        COMMAND ${CMAKE_COMMAND} -E copy "${SGCORE_BINS}/$<CONFIGURATION>/sgcore.dll" "$<TARGET_FILE_DIR:${PROJECT_NAME}>"
    )
endif()

message(STATUS "SenseGlove C++ library setup complete.")
