#
# @file       check_gdb_val_type.py
# @brief
# @date       2023-08-05
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import re

def check_gdb_val_type(pattern_s):
    pattern = re.compile(pattern_s)

    def helper(init_fun):

        def wrapper(self, gdb_val):
            gdb_val_type_s = str(gdb_val.type.strip_typedefs())
            if not pattern.match(gdb_val_type_s):
                raise TypeError("Expected: \"{}\", got: \"{}\"".format(pattern_s, gdb_val_type_s))
            init_fun(self, gdb_val)

        return wrapper

    return helper
