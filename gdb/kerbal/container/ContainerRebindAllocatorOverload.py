#
# @file       ContainerRebindAllocatorOverload.py
# @brief
# @date       2022-04-07
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.base_class_types import base_class_types
from kerbal.register_class import register_class

from kerbal.utility.MemberCompressHelper import MemberCompressHelper


@register_class("^kerbal::container::detail::container_rebind_allocator_overload<.*,.*>$")
class ContainerRebindAllocatorOverload(MemberCompressHelper):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        member_compress_helper_type = base_class_types(val.type)[0]  # member_compress_helper
        MemberCompressHelper.__init__(self, val.cast(member_compress_helper_type))

    @staticmethod
    def get_printer(val):
        return ContainerRebindAllocatorOverloadPrinter(val)


class ContainerRebindAllocatorOverloadPrinter(ContainerRebindAllocatorOverload):

    def dump(self):
        d = []

        if self.is_compressed():
            d.append(("rebind allocator (compressed)", self.member()))
        else:
            d.append(("rebind allocator", self.member()))

        return d

    def children(self):
        return self.dump()
