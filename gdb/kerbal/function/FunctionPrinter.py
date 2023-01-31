#
# @file       FunctionPrinter.py
# @brief
# @date       2022-06-13
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


class FunctionAllocatorOverload(MemberCompressHelper):

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


# @register_printer("^kerbal::function::basic_function<.*,.*,.*>$")
class FunctionPrinter(FunctionAllocatorOverload):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        FunctionAllocatorOverload.__init__(self, val)
        self.__val = val

    def dump(self):
        d = dict(self.children())
        return d

    def manage_type(self):
        manage_table = self.__val["k_mtable"]
        print(manage_table.type)
        manage_table_in_str = str(manage_table)
        print(manage_table_in_str)
        # 0x5639c9685ce0 <kerbal::function::detail::function_manager_collection<test_function(kerbal::test::assert_record&)::{lambda()#1}, std::allocator<char>, 8ul, 8ul, void>::mtable>
        pattern = "<(.*)::mtable>$"
        function_manager_collection_type_in_str = re.findall(pattern, manage_table_in_str)[0]
        print(function_manager_collection_type_in_str)
        function_manager_collection_type = gdb.lookup_type(function_manager_collection_type_in_str)
        print(function_manager_collection_type)
        manage_type = function_manager_collection_type.template_arguments(0)
        print(manage_type)
        return manage_type

    void_type = gdb.lookup_type("void")

    def children(self):
        for e in FunctionAllocatorOverload.dump(self):
            yield e

        manage_type = self.manage_type()
        yield "manage type", manage_type.name
        has_value = manage_type != FunctionPrinter.void_type
        if has_value:
            manage_type_ptr = manage_type.pointer()
            yield "value (if inlined)", self.__val["k_storage"]["buffer"].address.cast(manage_type_ptr).dereference()
            yield "value (if not inlined)", self.__val["k_storage"]["ptr"].cast(manage_type_ptr).dereference()
