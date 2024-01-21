#
# @file       CMakeLists.txt
# @brief
# @date       2023-02-06
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

set(KERBAL_GDB_PRETTY_PRINTER_INSTALL_DIR ${CMAKE_INSTALL_DATADIR}/gdb)
install(
        DIRECTORY kerbal
        DESTINATION ${KERBAL_GDB_PRETTY_PRINTER_INSTALL_DIR}
)

set(generate_gdbinit_suggestion "${CMAKE_BINARY_DIR}/cpack/pretty_printer/gdb/generate_gdbinit_suggestion.cmake")
configure_file(
        generate_gdbinit_suggestion.cmake.in
        "${generate_gdbinit_suggestion}"
        @ONLY
)
