#
# @file       VectorAllocatorUnrelated.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_class import register_class


@register_class("^kerbal::container::detail::vector_allocator_unrelated<.*>$")
class VectorAllocatorUnrelated:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def size(self):
        return self.__val["k_size"]

    def capacity(self):
        return self.__val["k_capacity"]

    def at(self, idx):
        return self.__val["k_buffer"][idx]

    @staticmethod
    def get_printer(val):
        return VectorAllocatorUnrelatedPrinter(val)


class VectorAllocatorUnrelatedPrinter(VectorAllocatorUnrelated):

    def head(self):
        d = [
            ("capacity", self.capacity()),
            ("size", self.size()),
        ]
        return d

    def dump(self):
        d = dict(self.children())
        return d

    def each(self):
        i = 0
        sz = self.size()
        while i < sz:
            yield "[{}]".format(i), self.at(i)
            i = i + 1

    def children(self):
        for e in self.head():
            yield e

        for e in self.each():
            yield e
