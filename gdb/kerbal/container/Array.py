#
# @file       Array.py
# @brief
# @date       2021-08-25
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_class import register_class


@register_class("^kerbal::container::array<.*,.*>$")
class Array:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def size(self):
        return self.__val["k_data"].type.range()[1] + 1

    def at(self, idx):
        return self.__val["k_data"][idx]

    @staticmethod
    def get_printer(val):
        return ArrayPrinter(val)


class ArrayPrinter(Array):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        Array.__init__(self, val)

    def dump(self):
        d = dict(self.children())
        return d

    def each(self):
        for i in range(self.size()):
            yield "[{}]".format(i), self.at(i)

    def children(self):
        for e in self.each():
            yield e
