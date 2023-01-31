#
# @file       lookup.py
# @brief
# @date       2020-07-17
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb

from kerbal.register_printer import pattern_printer_type_list

value_type_str_to_printer_map = {}


def printer_lookup(cxx_value: gdb.Value):
    cxx_value_type = cxx_value.type.strip_typedefs().unqualified()
    s = str(cxx_value_type)

    if s not in value_type_str_to_printer_map:
        has_printer = False
        for pattern, printer_type in pattern_printer_type_list:
            if pattern.match(s):
                value_type_str_to_printer_map[s] = printer_type
                has_printer = True
                break
        if not has_printer:
            # print("There is no printer for " + s)
            value_type_str_to_printer_map[s] = None

    found_printer_type = value_type_str_to_printer_map[s]
    if found_printer_type is None:
        return None
    return found_printer_type(cxx_value)


gdb.pretty_printers.append(printer_lookup)
