#
# @file       AVLTypeOnlyPrinter.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_printer import register_printer
from kerbal.container.detail.AVLIterator import leftest_offspring
from kerbal.container.detail.AVLIterator import AVLIterator

import gdb


@register_printer("^kerbal::container::detail::avl_type_only<.*>$")
class AVLTypeOnlyPrinter:
    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def begin(self):
        return AVLIterator(leftest_offspring(self.__val["k_head"].address))

    def end(self):
        return AVLIterator(self.__val["k_head"].address)

    def head(self):
        d = [
            ("head", self.__val["k_head"]),
            ("size", self.__val["k_size"]),
        ]
        return d

    def dump(self):
        d = dict(self.children())
        return d

    def each(self):
        value_type = self.__val.type.template_argument(0)
        list_node_type = gdb.lookup_type("kerbal::container::detail::avl_node<{}>".format(str(value_type)))
        list_node_ptr_type = list_node_type.pointer()

        i = 0
        it = self.begin()
        end = self.end()

        print("it: ")
        print(it.current())
        print("end: ")
        print(end.current())

        while it != end:
            print(it.current())
            p_to_node = it.current().cast(list_node_ptr_type)
            yield "[{}]".format(i), p_to_node.dereference()
            i += 1
            it.forward()
            print(it != end)

    def children(self):
        for e in self.head():
            yield e

        for e in self.each():
            yield e

