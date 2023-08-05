#
# @file       AVLTypeOnly.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_class import register_class

from kerbal.container.detail.avl_base.AVLNode import leftest_offspring
from kerbal.container.detail.avl_base.AVLIterator import AVLIter

import gdb


@register_class("^kerbal::container::detail::avl_type_only<.*>$")
class AVLTypeOnly:
    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.val = val

    def begin(self):
        print("enter begin")
        return AVLIter(leftest_offspring(self.val["k_head"].address))

    def end(self):
        return AVLIter(self.val["k_head"].address)

    @staticmethod
    def get_printer(val):
        return AVLTypeOnlyPrinter(val)


class AVLTypeOnlyPrinter(AVLTypeOnly):
    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        super().__init__(val)

    def head(self):
        d = [
            ("head", self.val["k_head"]),
            ("size", self.val["k_size"]),
        ]
        return d

    def dump(self):
        d = dict(self.children())
        return d

    def each(self):
        value_type = self.val.type.template_argument(0)
        avl_node_type = gdb.lookup_type("kerbal::container::detail::avl_node<{}>".format(str(value_type)))
        avl_node_ptr_type = avl_node_type.pointer()

        i = 0
        it = self.begin()
        print("abc")
        end = self.end()

        print("xxx")
        print(it != end)
        while it != end:
            p_to_node = it.current.cast(avl_node_ptr_type)
            yield "[{}]".format(i), p_to_node.dereference()
            i += 1
            it.forward()

    def children(self):
        for e in self.head():
            yield e

        for e in self.each():
            yield e
