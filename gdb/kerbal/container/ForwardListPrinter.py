#
# @file       ForwardListPrinter.py
# @brief
# @date       2021-09-27
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.container.ContainerRebindAllocatorOverloadPrinter import ContainerRebindAllocatorOverloadPrinter
from kerbal.register_printer import register_printer

import gdb


class ForwardListIteratorPrinterBase:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def dump(self):
        value_type = self.__val.type.template_argument(0)
        fl_node_type = gdb.lookup_type("kerbal::container::detail::sl_node<{}>".format(str(value_type)))
        fl_node_ptr_type = fl_node_type.pointer()
        d = []
        current = self.__val["current"]
        if current:
            d.append(("*", current.cast(fl_node_ptr_type)["value"]))
        d.append(("current", current))
        return d

    def children(self):
        return self.dump()


@register_printer("^kerbal::container::detail::fl_iter<.*>$")
class ForwardListIteratorPrinter(ForwardListIteratorPrinterBase):
    pass


@register_printer("^kerbal::container::detail::fl_kiter<.*>$")
class ForwardListConstIteratorPrinter(ForwardListIteratorPrinterBase):
    pass


@register_printer("^kerbal::container::detail::fl_allocator_unrelated<.*>$")
class ForwardListAllocatorUnrelatedPrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def head(self):
        d = [
            ("head", self.__val["head_node"]),
        ]
        return d

    def dump(self):
        d = dict(self.children())
        return d

    def each(self):
        value_type = self.__val.type.template_argument(0)
        fl_node_type = gdb.lookup_type("kerbal::container::detail::sl_node<{}>".format(str(value_type)))
        fl_node_ptr_type = fl_node_type.pointer()

        i = 0
        p = self.__val["head_node"]["next"]
        while p:
            p_to_node = p.cast(fl_node_ptr_type)
            yield "[{}]".format(i), p_to_node.dereference()
            i += 1
            p = p["next"]

    def children(self):
        for e in self.head():
            yield e

        for e in self.each():
            yield e


@register_printer("^kerbal::container::forward_list<.*,.*>$")
class ForwardListPrinter(ContainerRebindAllocatorOverloadPrinter, ForwardListAllocatorUnrelatedPrinter):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        ContainerRebindAllocatorOverloadPrinter.__init__(self, val)
        ForwardListAllocatorUnrelatedPrinter.__init__(self, val)

    def dump(self):
        d = dict(self.children())
        return d

    def children(self):
        for e in ContainerRebindAllocatorOverloadPrinter.dump(self):
            yield e

        for e in self.head():
            yield e

        for e in self.each():
            yield e
