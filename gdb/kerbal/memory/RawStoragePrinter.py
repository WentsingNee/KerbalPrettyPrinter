#
# @file       RawStoragePrinter.py
# @brief
# @date       2021-10-02s
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_printer import register_printer


@register_printer("^kerbal::memory::raw_storage<.*>$")
class RawStoragePrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def value_type(self):
        return self.__val.type.template_argument(0)

    def raw_value(self):
        pointer_type = self.value_type().pointer()
        return self.__val["_K_storage"].address.reinterpret_cast(pointer_type).dereference()

    def dump(self):
        return "value", self.raw_value()

    def children(self):
        yield self.dump()
