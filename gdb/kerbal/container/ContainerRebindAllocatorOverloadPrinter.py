#
# @file       ContainerRebindAllocatorOverloadPrinter.py
# @brief
# @date       2022-04-07
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb

from kerbal.register_printer import register_printer
from kerbal.base_class_types import base_class_types
from kerbal.utility.MemberCompressHelperPrinter import MemberCompressHelper


@register_printer("^kerbal::container::detail::container_rebind_allocator_overload<.*,.*>$")
class ContainerRebindAllocatorOverloadPrinter(MemberCompressHelper):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        member_compress_helper_type = base_class_types(val.type)[0]  # member_compress_helper
        MemberCompressHelper.__init__(self, val.cast(member_compress_helper_type))

    def dump(self):
        d = []

        if self.is_compressed():
            d.append(("rebind allocator (compressed)", self.member()))
        else:
            d.append(("rebind allocator", self.member()))

        return d

    def children(self):
        return self.dump()

