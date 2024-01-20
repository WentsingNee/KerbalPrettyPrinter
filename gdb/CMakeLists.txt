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
        FILES_MATCHING
            PATTERN "*.py"
            PATTERN "__pycache__" EXCLUDE
)
