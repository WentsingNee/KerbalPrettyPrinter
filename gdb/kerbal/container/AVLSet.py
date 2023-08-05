#
# @file       AVLSet.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_class import register_class

from kerbal.container.detail.avl_base.AVLTypeOnly import AVLTypeOnlyPrinter
from kerbal.container.ContainerRebindAllocatorOverload import ContainerRebindAllocatorOverloadPrinter


# @register_class("^kerbal::container::avl_set<.*,.*,.*>$")
class AVLSet:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.val = val

    @staticmethod
    def get_printer(val):
        return AVLSetPrinter(val)


class AVLSetPrinter(ContainerRebindAllocatorOverloadPrinter, AVLTypeOnlyPrinter):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        ContainerRebindAllocatorOverloadPrinter.__init__(self, val)
        AVLTypeOnlyPrinter.__init__(self, val)

    def dump(self):
        d = dict(self.children())
        return d

    def children(self):
        for e in ContainerRebindAllocatorOverloadPrinter.dump(self):
            yield e

        for e in self.head():
            yield e

        for e in AVLTypeOnlyPrinter.each(self):
            yield e
