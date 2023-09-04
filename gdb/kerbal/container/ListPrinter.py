#
# @file       ListPrinter.py
# @brief
# @date       2020-04-11
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.base_class_types import base_class_types
from kerbal.container.ContainerRebindAllocatorOverloadPrinter import ContainerRebindAllocatorOverloadPrinter
from kerbal.register_printer import register_printer

import gdb


@register_printer("^kerbal::container::detail::list_node_base$")
class ListNodeBasePrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    void_type = gdb.lookup_type("void")
    void_ptr_type = void_type.pointer()

    def dump(self):
        d = [
            ("prev", self.__val["prev"].reinterpret_cast(ListNodeBasePrinter.void_ptr_type)),
            ("this", self.__val.address),
            ("next", self.__val["next"].reinterpret_cast(ListNodeBasePrinter.void_ptr_type)),
        ]
        return d

    def children(self):
        return self.dump()


@register_printer("^kerbal::container::detail::list_node<.*>$")
class ListNodePrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def dump(self):
        node_base_type = base_class_types(self.__val.type)[0]
        node_base_ptr_type = node_base_type.pointer()

        d = [
            ("value", self.__val["value"]),
            ("node base", self.__val.address.cast(node_base_ptr_type).dereference()),
        ]
        return d

    def children(self):
        return self.dump()


class ListIteratorPrinterBase:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def dump(self):
        value_type = self.__val.type.template_argument(0)
        list_node_type = gdb.lookup_type("kerbal::container::detail::list_node<{}>".format(str(value_type)))
        list_node_ptr_type = list_node_type.pointer()
        d = []
        current = self.__val["current"]
        if current:
            d.append(("*", current.cast(list_node_ptr_type)["value"]))
        d.append(("current", current))
        return d

    def children(self):
        return self.dump()


@register_printer("^kerbal::container::detail::list_iter<.*>$")
class ListIteratorPrinter(ListIteratorPrinterBase):
    pass


@register_printer("^kerbal::container::detail::list_kiter<.*>$")
class ListConstIteratorPrinter(ListIteratorPrinterBase):
    pass


@register_printer("^kerbal::container::detail::list_allocator_unrelated<.*>$")
class ListAllocatorUnrelatedPrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def head(self):
        d = [
            ("head", self.__val["k_head"]),
        ]
        return d

    def dump(self):
        d = dict(self.children())
        return d

    def each(self):
        value_type = self.__val.type.template_argument(0)
        list_node_type = gdb.lookup_type("kerbal::container::detail::list_node<{}>".format(str(value_type)))
        list_node_ptr_type = list_node_type.pointer()

        i = 0
        p = self.__val["k_head"]["next"]
        while p != self.__val["k_head"].address:
            p_to_node = p.cast(list_node_ptr_type)
            yield "[{}]".format(i), p_to_node.dereference()
            i += 1
            p = p["next"]

    def children(self):
        for e in self.head():
            yield e

        for e in self.each():
            yield e


@register_printer("^kerbal::container::list<.*,.*>$")
class ListPrinter(ContainerRebindAllocatorOverloadPrinter, ListAllocatorUnrelatedPrinter):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        ContainerRebindAllocatorOverloadPrinter.__init__(self, val)
        ListAllocatorUnrelatedPrinter.__init__(self, val)

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
