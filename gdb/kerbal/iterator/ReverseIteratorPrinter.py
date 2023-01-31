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

import gdb

from kerbal.register_printer import register_printer


@register_printer("^kerbal::iterator::reverse_iterator<.*>$")
class ReverseIteratorPrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def dump(self):
        reverse_iterator_type = self.__val.type.fields()[0].type
        reverse_iterator_base_type = reverse_iterator_type.fields()[0].type
        reverse_iterator_base_ptr_type = reverse_iterator_base_type.pointer()

        is_inplace = reverse_iterator_base_type.template_argument(1)

        base = self.__val.address.cast(reverse_iterator_base_ptr_type).dereference()
        if is_inplace:
            d = [
                ("base (in_place)", base)
            ]
        else:
            d = [
                ("base (not in_place)", base)
            ]
        return d

    def children(self):
        return self.dump()
