# CMakeList to create a project with an executable, linked to the SGCore C++ Library as a .dll file

cmake_minimum_required (VERSION 3.10)
project("glove_data_acquisition" VERSION 1.0.0) # Adjust the project name as necessary

# Our main project will be an executable with the main.cpp in the same folder as this file.
add_executable(${PROJECT_NAME} glove_data_acquisition.cpp)    # Adjust the name of .cpp file as necessary

# Set this as the startup project if we're using Visual Studio Code
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ${PROJECT_NAME})

message(STATUS "Attempting to add the SGCoreCpp project at ${CMAKE_CURRENT_SOURCE_DIR}")

# Include the .cmake file that links and include SGCoreCpp in this project
include(${SGCORECPP_PATH}/LinkSGCoreCpp.cmake)

message(STATUS "Done!")