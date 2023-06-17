#
# @file       OptionalPrinter.py
# @brief
# @date       2022-01-03
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.base_class_types import base_class_types
from kerbal.memory.RawStoragePrinter import RawStoragePrinter
from kerbal.register_printer import register_printer


@register_printer("^kerbal::optional::optional<.*>$")
class OptionalPrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def has_value(self):
        """
        @return: bool
        """
        return self.__val["k_has_value"]

    def dump(self):
        optional_base_type = base_class_types(self.__val.type)[0]
        raw_storage_type = optional_base_type.fields()[0].type
        raw_storage = self.__val.cast(raw_storage_type)
        raw_storage_printer = RawStoragePrinter(raw_storage)
        d = [
            ("has value", self.has_value()),
            ("value (if has)", raw_storage_printer.raw_value())
        ]
        return d

    def children(self):
        return self.dump()
