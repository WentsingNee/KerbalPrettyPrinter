#
# @file       AVLSetPrinter.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_printer import register_printer
from kerbal.container.detail.AVLTypeOnlyPrinter import AVLTypeOnlyPrinter
from kerbal.container.ContainerRebindAllocatorOverloadPrinter import ContainerRebindAllocatorOverloadPrinter


@register_printer("^kerbal::container::avl_set<.*,.*,.*>$")
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

        for e in self.each():
            yield e

