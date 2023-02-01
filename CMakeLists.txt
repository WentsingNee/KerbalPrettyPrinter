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

if (CMAKE_CXX_PLATFORM_ID MATCHES "Linux")
    set (KERBAL_INSTALL_GDB_PRETTY_PRINTER_DEFAULT ON)
endif ()

if (CMAKE_CXX_PLATFORM_ID MATCHES "Windows")
    set (KERBAL_INSTALL_NATVIS_PRETTY_PRINTER_DEFAULT ON)
endif ()


# GDB pretty printer
option(KERBAL_INSTALL_GDB_PRETTY_PRINTER "install GDB pretty printer" ${KERBAL_INSTALL_GDB_PRETTY_PRINTER_DEFAULT})

if (KERBAL_INSTALL_GDB_PRETTY_PRINTER)
    add_subdirectory(gdb)
endif ()


# natvis pretty printer
option(KERBAL_INSTALL_NATVIS_PRETTY_PRINTER "install natvis pretty printer" ${KERBAL_INSTALL_NATVIS_PRETTY_PRINTER_DEFAULT})

if (KERBAL_INSTALL_NATVIS_PRETTY_PRINTER)
    add_subdirectory(natvis)
endif ()
