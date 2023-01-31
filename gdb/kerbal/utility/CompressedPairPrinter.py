#
# @file       CompressedPairPrinter.py
# @brief
# @date       2020-07-17
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


@register_printer("^kerbal::utility::compressed_pair<.*,.*>$")
class CompressedPairPrinter:

    def __init__(self, val: gdb.Value):
        self.__val = val

    def dump(self):

        self_type = self.__val.type

        super_type = [
            base_class_types(self_type)[0],
            base_class_types(self_type)[1],
        ]

        helper = [
            MemberCompressHelper(self.__val.cast(super_type[0])),
            MemberCompressHelper(self.__val.cast(super_type[1])),
        ]

        d = []

        if helper[0].is_compressed():
            d.append(("first (compressed)", helper[0].member()))
        else:
            d.append(("first", helper[0].member()))

        if helper[1].is_compressed():
            d.append(("second (compressed)", helper[1].member()))
        else:
            d.append(("second", helper[1].member()))

        return d

    def children(self):
        return self.dump()
