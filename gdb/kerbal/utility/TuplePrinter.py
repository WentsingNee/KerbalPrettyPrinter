#
# @file       TuplePrinter.py
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


@register_printer("^kerbal::utility::tuple<.*>$")
class TuplePrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val
        self.__member_compress_helpers = []

        tuple_impl = base_class_types(self.__val.type)[0]
        for base in base_class_types(tuple_impl):
            self.__member_compress_helpers.append(MemberCompressHelper(self.__val.cast(base)))

    def size(self):
        return len(self.__member_compress_helpers)

    def get(self, idx):
        """
        @param idx: int
        """
        helper = self.__member_compress_helpers[idx]
        return helper.member()

    def i_is_compressed(self, idx):
        """
        @param idx: int
        @return: bool
        """
        helper = self.__member_compress_helpers[idx]
        return helper.is_compressed()

    def dump(self):

        d = [
            ("tuple_size", self.size())
        ]
        for idx in range(self.size()):
            member = self.get(idx)
            if self.i_is_compressed(idx):
                d.append(("<{}> (compressed)".format(idx), member))
            else:
                d.append(("<{}>".format(idx), member))

            idx += 1

        return d

    def children(self):
        return self.dump()

