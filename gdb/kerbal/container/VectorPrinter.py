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

from kerbal.container.ContainerAllocatorOverloadPrinter import ContainerAllocatorOverloadPrinter
from kerbal.register_printer import kerbal_printer


@kerbal_printer.register_template_printer("^kerbal::container::detail::vector_allocator_unrelated<.*>$")
class VectorTypeOnlyPrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def size(self):
        return self.__val["k_size"]

    def capacity(self):
        return self.__val["k_capacity"]

    def data(self):
        return self.__val["k_buffer"]

    def __getitem__(self, i):
        return self.data()[i]

    def head(self):
        yield "capacity", self.capacity()
        yield "size", self.size()

    def dump(self):
        d = dict(self.children())
        return d

    def each(self):
        for i in range(self.size()):
            yield f"[{i}]", self[i]

    def children(self):
        for e in self.head():
            yield e

        for e in self.each():
            yield e


@kerbal_printer.register_template_printer("^kerbal::container::vector<.*,.*>$")
class VectorPrinter(ContainerAllocatorOverloadPrinter, VectorTypeOnlyPrinter):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        ContainerAllocatorOverloadPrinter.__init__(self, val)
        VectorTypeOnlyPrinter.__init__(self, val)

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
