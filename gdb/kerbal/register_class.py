#
# @file       register_class.py
# @brief
# @date       2020-07-17
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import re

pattern_class_type_list = []


def register_class(pattern_s):
    """
    @param pattern_s: str
    """

    def pattern_helper(py_type):
        print("binding type pattern: {} with class: {}".format(pattern_s, str(py_type)))
        pattern = re.compile(pattern_s)
        pattern_class_type_list.append((pattern, py_type))
        return py_type

    return pattern_helper
