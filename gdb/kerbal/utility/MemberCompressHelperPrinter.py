#
# @file       MemberCompressHelperPrinter.py
# @brief
# @date       2021-05-28
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import re

from kerbal.base_class_types import base_class_types
from kerbal.register_printer import register_printer


class MemberCompressHelper:

    @staticmethod
    def cast_inheritance_to_member_compress_helper(val):
        """
        @param val: gdb.Value
        @return: gdb.Value
        """
        def impl(val):
            """
            @param val: gdb.Value
            """
            value_type = val.type
            if re.match(r"^kerbal::utility::member_compress_helper<.*,.*>$", value_type.name):
                return val
            for base_type in base_class_types(value_type):
                value_after_cast = impl(val.cast(base_type))
                if not value_after_cast is None:
                    return value_after_cast
            return None

        value_after_cast = impl(val)
        if value_after_cast is None:
            raise Exception("type: {} is not member_compress_helper".format(val.type.name))
        return value_after_cast

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = MemberCompressHelper.cast_inheritance_to_member_compress_helper(val)

    def is_compressed(self):
        """
        @return: bool
        """
        self_type = self.__val.type

        if self_type.has_key("k_member"):
            return False

        super_type = base_class_types(self_type)[0]
        return not super_type.has_key("k_member")

    def value_type(self):
        """
        @return: gdb.Type
        """
        self_type = self.__val.type
        return self_type.template_argument(0)

    def member(self):
        """
        @return: gdb.Value
        """
        if self.is_compressed():
            return self.__val.cast(self.value_type())
        else:
            return self.__val["k_member"]


@register_printer("^kerbal::utility::member_compress_helper<.*,.*>$")
class MemberCompressHelperPrinter(MemberCompressHelper):

    def dump(self):
        d = []

        if self.is_compressed():
            d.append(("member (compressed)", self.member()))
        else:
            d.append(("member", self.member()))

        return d

    def children(self):
        return self.dump()
