#
# @file       ListNode.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb

from kerbal.base_class_types import base_class_types
from kerbal.register_class import register_class

from kerbal.utility.MemberCompressHelper import MemberCompressHelper


@register_class("kerbal::container::detail::list_node_base")
class ListNodeBase:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def prev(self):
        return self.__val["prev"]

    def this(self):
        return self.__val.address

    def next(self):
        return self.__val["next"]

    @staticmethod
    def get_printer(val):
        return ListNodeBasePrinter(val)


class ListNodeBasePrinter(ListNodeBase):

    void_type = gdb.lookup_type("void")
    void_ptr_type = void_type.pointer()

    def dump(self):
        d = [
            ("prev", self.prev().reinterpret_cast(ListNodeBasePrinter.void_ptr_type)),
            ("this", self.this()),
            ("next", self.next().reinterpret_cast(ListNodeBasePrinter.void_ptr_type)),
        ]
        return d

    def children(self):
        return self.dump()


@register_class("^kerbal::container::detail::list_node<.*>$")
class ListNode(ListNodeBase, MemberCompressHelper):

    def __init__(self, val):
        ListNodeBase.__init__(self, val)
        MemberCompressHelper.__init__(self, val)
        self.node_base_type, self.member_compress_helper_type = base_class_types(val.type)

    def as_node_base(self):
        return self._ListNodeBase__val.cast(self.node_base_type)

    @staticmethod
    def get_printer(val):
        return ListNodePrinter(val)


class ListNodePrinter(ListNode):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        super().__init__(val)

    def dump(self):
        d = []
        d.append(("node base", self.as_node_base()))
        if self.is_compressed():
            d.append(("value (compressed)", self.member()))
        else:
            d.append(("value", self.member()))

        return d

    def children(self):
        return self.dump()
