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

import re

pattern_printer_type_list = []


def register_printer(pattern_s):
    """
    @param pattern_s: str
    """
    def pattern_helper(printer_type):
        print("binding type pattern: {} with printer: {}".format(pattern_s, str(printer_type)))
        pattern = re.compile(pattern_s)
        pattern_printer_type_list.append((pattern, printer_type))
        return printer_type

    return pattern_helper
