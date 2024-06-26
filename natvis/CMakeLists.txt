#
# @file       CMakeLists.txt
# @brief
# @date       2023-02-01
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

set(KERBAL_PRETTY_PRINTER_NATVIS_INSTALL_DIR "${CMAKE_INSTALL_DATADIR}/Visualizers")

message(STATUS "Configuring natvis files")

file(GLOB_RECURSE natvis_files RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}/ "*.natvis")
foreach (file IN LISTS natvis_files)
    string(REPLACE "/" "." natvis_install_name "${file}")
    set(natvis_install_name "kerbal.${natvis_install_name}")
    message(STATUS "Add natvis ${natvis_install_name} <= ${CMAKE_CURRENT_SOURCE_DIR}/kerbal/${file}")
    install(
            FILES ${file}
            DESTINATION ${KERBAL_PRETTY_PRINTER_NATVIS_INSTALL_DIR}
            RENAME ${natvis_install_name}
    )
endforeach ()

message(STATUS "Configuring natvis files complete\n")
