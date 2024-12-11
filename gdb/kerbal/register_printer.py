#
# @file       register_printer.py
# @brief
# @date       2020-07-17
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb
import re


class __PrinterLookup:

    def __init__(self):
        self.type_name_to_printer = {}
        self.pattern_printer_type_list = []

    def load_printer_in_pattern(self, type_name):
        found_printer_type = None
        for pattern, printer_type in self.pattern_printer_type_list:
            if pattern.match(type_name):
                found_printer_type = printer_type
                break
        self.type_name_to_printer[type_name] = found_printer_type
        return found_printer_type

    def __call__(self, cxx_value):
        """
        @param cxx_value: gdb.Value
        """
        cxx_value_type = cxx_value.type.strip_typedefs().unqualified()
        type_name = str(cxx_value_type)

        if type_name not in self.type_name_to_printer:
            found_printer_type = self.load_printer_in_pattern(type_name)
        else:
            found_printer_type = self.type_name_to_printer[type_name]
        if found_printer_type is None:
            return None
        return found_printer_type(cxx_value)

    def register_template_printer(self, type_pattern_s):
        """
        @param type_pattern_s: str
        """
        def pattern_helper(printer_type):
            print("binding type pattern: {} with printer: {}".format(type_pattern_s, str(printer_type)))
            pattern = re.compile(type_pattern_s)
            self.pattern_printer_type_list.append((pattern, printer_type))
            return printer_type

        return pattern_helper

    def register_printer(self, type_name):
        """
        @param type_name: str
        """
        def pattern_helper(printer_type):
            print("binding type: {} with printer: {}".format(type_name, str(printer_type)))
            self.type_name_to_printer[type_name] = printer_type
            return printer_type

        return pattern_helper


kerbal_printer = __PrinterLookup()
gdb.pretty_printers.append(kerbal_printer)
