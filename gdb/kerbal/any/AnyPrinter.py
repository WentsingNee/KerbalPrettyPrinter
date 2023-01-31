#
# @file       AnyPrinter.py
# @brief
# @date       2021-08-27
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb
import re

from kerbal.register_printer import register_printer
from kerbal.base_class_types import base_class_types
from kerbal.utility.MemberCompressHelperPrinter import MemberCompressHelper


class AnyAllocatorOverload(MemberCompressHelper):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        member_compress_helper_type = base_class_types(val.type)[0]  # member_compress_helper
        MemberCompressHelper.__init__(self, val.cast(member_compress_helper_type))

    def dump(self):
        d = []

        if self.is_compressed():
            d.append(("void allocator (compressed)", self.member()))
        else:
            d.append(("void allocator", self.member()))

        return d


@register_printer("^kerbal::any::basic_any<.*,.*,.*>$")
class AnyPrinter(AnyAllocatorOverload):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        AnyAllocatorOverload.__init__(self, val)
        self.__val = val

    def dump(self):
        d = dict(self.children())
        return d

    def manage_type(self):
        manage_table = self.__val["k_mtable"]
        manage_table_in_str = str(manage_table)
        print(manage_table_in_str)
        # "0x55db33d4bcc0 <kerbal::any::detail::any_manager_collection<int, std::allocator<char>, 8ul, 8ul>::mtable>"
        pattern = "<kerbal::any::detail::any_manager_collection<(.*), .*, .*, .*>::mtable>"
        manage_type_in_str = re.findall(pattern, manage_table_in_str)[0]
        print(manage_type_in_str)
        manage_type = gdb.lookup_type(manage_type_in_str)
        return manage_type

    void_type = gdb.lookup_type("void")

    def children(self):
        for e in AnyAllocatorOverload.dump(self):
            yield e

        manage_type = self.manage_type()
        yield "manage type", manage_type.name
        has_value = manage_type != AnyPrinter.void_type
        if has_value:
            manage_type_ptr = manage_type.pointer()
            yield "value (if inlined)", self.__val["k_storage"]["buffer"].address.cast(manage_type_ptr).dereference()
            yield "value (if not inlined)", self.__val["k_storage"]["ptr"].cast(manage_type_ptr).dereference()
