#
# @file       ListAllocatorUnrelated.py
# @brief
# @date       2023-08-05
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb

from kerbal.register_class import register_class

from kerbal.container.detail.list_base.ListIterator import ListIter


@register_class("^kerbal::container::detail::list_allocator_unrelated<.*>$")
class ListAllocatorUnrelated:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.val = val
        self.value_type = val.type.template_argument(0)

        # value_type = self.val.type.target().template_argument(0)
        # self.const_iterator_type = gdb.lookup_type("kerbal::container::detail::list_kiter<{}>".format(value_type))

    def begin(self):
        return ListIter(self.val["head_node"]["next"], self.value_type)

    def end(self):
        return ListIter(self.val["head_node"].address, self.value_type)

    @staticmethod
    def get_printer(val):
        return ListAllocatorUnrelatedPrinter(val)


class ListAllocatorUnrelatedPrinter(ListAllocatorUnrelated):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        super().__init__(val)

    def head(self):
        d = [
            ("head", self.val["head_node"]),
        ]
        return d

    def dump(self):
        d = dict(self.children())
        return d

    def each(self):
        i = 0
        it = self.begin()
        end = self.end()
        while it != end:
            yield "[{}]".format(i), it.dereference()
            i += 1
            it.forward()

    def children(self):
        for e in self.head():
            yield e

        for e in self.each():
            yield e
