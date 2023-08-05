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
from kerbal.register_class import register_class


@register_class("^kerbal::iterator::reverse_iterator<.*,.*>$")
class ReverseIterator:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

        self.__is_inplace = self.__val.type.template_argument(1)
        reverse_iterator_base_type = self.__val.type.template_argument(0)
        self.__reverse_iterator_base_ptr_type = reverse_iterator_base_type.pointer()

    def is_inplace(self):
        return self.__is_inplace

    def base(self):
        return self.__val.address.cast(self.__reverse_iterator_base_ptr_type).dereference()

    @staticmethod
    def get_printer(val):
        return ReverseIteratorPrinter(val)


class ReverseIteratorPrinter(ReverseIterator):

    def dump(self):
        base = self.base()
        d = []
        if self.is_inplace():
            d.append(("base (in_place)", base))
        else:
            d.append(("base (not in_place)", base))
        return d

    def children(self):
        return self.dump()
