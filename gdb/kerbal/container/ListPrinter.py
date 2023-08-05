#
# @file       ListPrinter.py
# @brief
# @date       2020-04-11
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.container.ContainerRebindAllocatorOverload import ContainerRebindAllocatorOverloadPrinter
from kerbal.register_printer import register_printer

import gdb


# @register_printer("^kerbal::container::list<.*,.*>$")
# class ListPrinter(ContainerRebindAllocatorOverloadPrinter, ListAllocatorUnrelatedPrinter):
#
#     def __init__(self, val):
#         """
#         @param val: gdb.Value
#         """
#         ContainerRebindAllocatorOverloadPrinter.__init__(self, val)
#         ListAllocatorUnrelatedPrinter.__init__(self, val)
#
#     def dump(self):
#         d = dict(self.children())
#         return d
#
#     def children(self):
#         for e in ContainerRebindAllocatorOverloadPrinter.dump(self):
#             yield e
#
#         for e in self.head():
#             yield e
#
#         for e in self.each():
#             yield e
