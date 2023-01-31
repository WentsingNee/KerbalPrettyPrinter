#
# @file       VectorPrinter.py
# @brief
# @date       2021-08-24
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb

from kerbal.register_printer import register_printer
from kerbal.base_class_types import base_class_types
from kerbal.container.ContainerAllocatorOverloadPrinter import ContainerAllocatorOverloadPrinter


@register_printer("^kerbal::container::detail::vector_allocator_unrelated<.*>$")
class VectorAllocatorUnrelatedPrinter:

    def __init__(self, val: gdb.Value):
        self.__val = val

    def size(self):
        return self.__val["_K_size"]

    def head(self):
        d = [
            ("capacity", self.__val["_K_capacity"]),
            ("size", self.__val["_K_size"]),
        ]
        return d

    def dump(self):
        d = dict(self.children())
        return d

    def each(self):
        i = 0
        sz = self.size()
        while i < sz:
            yield "[{}]".format(i), self.__val["_K_buffer"][i]
            i = i + 1

    def children(self):
        for e in self.head():
            yield e

        for e in self.each():
            yield e


@register_printer("^kerbal::container::vector<.*,.*>$")
class VectorPrinter(ContainerAllocatorOverloadPrinter, VectorAllocatorUnrelatedPrinter):

    def __init__(self, val: gdb.Value):
        ContainerAllocatorOverloadPrinter.__init__(self, val)
        VectorAllocatorUnrelatedPrinter.__init__(self, val)

    def dump(self):
        d = dict(self.children())
        return d

    def children(self):
        for e in ContainerAllocatorOverloadPrinter.dump(self):
            yield e

        for e in self.head():
            yield e

        for e in self.each():
            yield e
