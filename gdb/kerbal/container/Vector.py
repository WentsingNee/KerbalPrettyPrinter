#
# @file       Vector.py
# @brief
# @date       2021-08-24
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_class import register_class

from kerbal.container.ContainerAllocatorOverload import ContainerAllocatorOverloadPrinter
from kerbal.container.detail.vector_base.VectorAllocatorUnrelated import VectorAllocatorUnrelatedPrinter


@register_class("^kerbal::container::vector<.*,.*>$")
class Vector:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    @staticmethod
    def get_printer(val):
        return VectorPrinter(val)


class VectorPrinter(ContainerAllocatorOverloadPrinter, VectorAllocatorUnrelatedPrinter):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        ContainerAllocatorOverloadPrinter.__init__(self, val)
        VectorAllocatorUnrelatedPrinter.__init__(self, val)

    def dump(self):
        d = dict(self.children())
        return d

    def children(self):
        for e in ContainerAllocatorOverloadPrinter.dump(self):
            yield e

        for e in VectorAllocatorUnrelatedPrinter.head(self):
            yield e

        for e in VectorAllocatorUnrelatedPrinter.each(self):
            yield e
