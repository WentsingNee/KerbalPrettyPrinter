#
# @file       AVLNodePrinter.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_printer import register_printer

import gdb


@register_printer("^kerbal::container::detail::avl_head_node")
class AVLHeadNodePrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def dump(self):
        d = [
            ("left", self.__val["left"]),
        ]
        return d

    def children(self):
        return self.dump()


@register_printer("^kerbal::container::detail::avl_node_base$")
class AVLNodeBasePrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def dump(self):
        d = [
            ("left", self.__val["left"]),
            ("right", self.__val["right"]),
            ("parent", self.__val["parent"]),
            ("height", self.__val["height"]),
        ]
        return d

    def children(self):
        return self.dump()