#
# @file       base_class_types.py
# @brief
# @date       2021-05-29
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb


def base_class_types(type: gdb.Type):
    r = []
    for field in type.fields():
        if field.is_base_class:
            r.append(field.type)

    return r
