#
# @file       ListIterator.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb

from kerbal.base_class_types import base_class_types
from kerbal.check_gdb_val_type import check_gdb_val_type
from kerbal.register_class import register_class

from kerbal.utility.MemberCompressHelper import MemberCompressHelper


class ListIter:

    def __init__(self, current, value_type):
        self.__current = current
        self.list_node_type = gdb.lookup_type("kerbal::container::detail::list_node<{}>".format(str(value_type)))
        self.node_base_type, self.member_compress_helper_type = base_class_types(self.list_node_type)

    def dereference(self):
        as_member_compress_helper = self.__current.dereference().cast(self.list_node_type).cast(self.member_compress_helper_type)
        member_compress_helper = MemberCompressHelper(as_member_compress_helper)
        return member_compress_helper.member()

    def current(self):
        return self.__current

    def next(self):
        return ListIter(self.__current["next"])

    def forward(self):
        self.__current = self.__current["next"]

    def prev(self):
        return ListIter(self.__current["prev"])

    def retreat(self):
        self.__current = self.__current["prev"]

    def __eq__(self, rhs):
        return self.__current == rhs.current

    def __ne__(self, rhs):
        return self.__current != rhs.current


@register_class("^kerbal::container::detail::list_(k)?iter<.*>$")
class ListIterator(ListIter):

    @check_gdb_val_type("^kerbal::container::detail::list_(k)?iter<.*>$")
    def __init__(self, val):
        """
        @param val: gdb.Value
        """

        value_type = val.type.template_argument(0)
        super().__init__(val["current"], value_type)

        self.__val = val

    def get_val(self):
        return self.__val

    @staticmethod
    def get_printer(val):
        return ListIteratorPrinter(val)


class ListIteratorPrinter(ListIterator):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        super().__init__(val)

    def dump(self):
        d = []
        current = self.current()
        if current:
            d.append(("*", self.dereference()))
            d.append(("current", current))
        return d

    def children(self):
        return self.dump()
