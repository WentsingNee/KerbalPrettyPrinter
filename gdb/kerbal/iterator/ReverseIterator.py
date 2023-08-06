#
# @file       ReverseIteratorPrinter.py
# @brief
# @date       2020-08-16
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.base_class_types import base_class_types
from kerbal.lookup import class_lookup
from kerbal.register_class import register_class


@register_class("^kerbal::iterator::reverse_iterator<.*,.*>$")
class ReverseIterator:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

        self.__is_inplace = self.__val.type.template_argument(1)
        self.__base_type = self.__val.type.template_argument(0)

    def is_inplace(self):
        return self.__is_inplace

    def actual(self):
        base = self.base()
        binded_type_of_base = class_lookup(base)
        if binded_type_of_base is None:
            return None

        binded_base_cxx_val = binded_type_of_base(base)

        if not self.__is_inplace:
            print(binded_base_cxx_val.current())
            binded_base_cxx_val.retreat()
            print(binded_base_cxx_val.current())

        print(binded_base_cxx_val.current())
        return binded_base_cxx_val.get_val()

    def base(self):
        return self.__val["iter"]

    @staticmethod
    def get_printer(val):
        return ReverseIteratorPrinter(val)


class ReverseIteratorPrinter(ReverseIterator):

    def dump(self):
        base = self.base()
        d = []
        d.append(("actual", self.actual()))
        if self.is_inplace():
            d.append(("base (in_place)", base))
        else:
            d.append(("base (not in_place)", base))
        return d

    def children(self):
        return self.dump()
