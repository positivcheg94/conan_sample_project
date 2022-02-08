add_library(sample_lib)

target_sources(sample_lib
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include/sample_lib/lib.hpp
        ${CMAKE_CURRENT_SOURCE_DIR}/src/lib.cpp
)

target_include_directories(sample_lib
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)
