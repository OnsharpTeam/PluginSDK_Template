set(PLUGIN_CONFIG_INCLUDE_DIR "${CMAKE_CURRENT_BINARY_DIR}/config_headers")

if(UNIX)
    link_libraries(stdc++fs)
endif()

configure_file(
        "version.hpp.in"
        "${PLUGIN_CONFIG_INCLUDE_DIR}/version.hpp"
        @ONLY
)

add_library(PluginSDK_Template MODULE
        Plugin.cpp
        Plugin.hpp
        Singleton.hpp
        PluginInterface.cpp
)

target_include_directories(PluginSDK_Template PRIVATE
        ${PLUGIN_CONFIG_INCLUDE_DIR}
        ${HORIZONSDK_INCLUDE_DIR}
)

set_property(TARGET PluginSDK_Template PROPERTY PREFIX "")
set_property(TARGET PluginSDK_Template PROPERTY OUTPUT_NAME "PluginSDK_Template")

set_property(TARGET PluginSDK_Template PROPERTY CXX_STANDARD 17)
set_property(TARGET PluginSDK_Template PROPERTY CXX_STANDARD_REQUIRED ON)

if(MSVC)
    target_compile_definitions(PluginSDK_Template PRIVATE
            _CRT_SECURE_NO_WARNINGS
            NOMINMAX
    )
endif()

# increase warning levels
if (MSVC)
    target_compile_options(PluginSDK_Template PRIVATE
            /W4
            /WX
            /permissive-
            /wd4505
    )
elseif(UNIX)
    target_compile_options(PluginSDK_Template PRIVATE
            -Wall
            -Wextra
            -pedantic
            -Werror
            -Wno-unused-variable
            -Wno-unused-function
    )
endif()

target_link_libraries(PluginSDK_Template ${HORIZONSDK_LIBRARY})

if(UNIX)
    if(NOT APPLE)
        target_link_libraries(PluginSDK_Template rt)
    endif()

    set_target_properties(PluginSDK_Template PROPERTIES
            INSTALL_RPATH "$ORIGIN/..:$ORIGIN/")
endif()

install(TARGETS PluginSDK_Template DESTINATION "plugins/")

set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})
if(WIN32)
    set(CPACK_GENERATOR ZIP)
else()
    set(CPACK_GENERATOR TGZ)
endif()

include(CPack)