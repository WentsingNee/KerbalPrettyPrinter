#
# @file       SingleListPrinter.py
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
from kerbal.container.ContainerRebindAllocatorOverloadPrinter import ContainerRebindAllocatorOverloadPrinter


@register_printer("^kerbal::container::detail::sl_node_base$")
class SingleListNodeBasePrinter:

    def __init__(self, val: gdb.Value):
        self.__val = val

    void_type = gdb.lookup_type("void")
    void_ptr_type = void_type.pointer()

    def dump(self):
        d = [
            ("this", self.__val.address),
            ("next", self.__val["next"].reinterpret_cast(SingleListNodeBasePrinter.void_ptr_type)),
        ]
        return d

    def children(self):
        return self.dump()


@register_printer("^kerbal::container::detail::sl_node<.*>$")
class SingleListNodePrinter:

    def __init__(self, val: gdb.Value):
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


@register_printer("^kerbal::container::detail::sl_allocator_unrelated<.*>$")
class SingleListAllocatorUnrelatedPrinter:

    def __init__(self, val: gdb.Value):
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
        sl_node_type = gdb.lookup_type("kerbal::container::detail::sl_node<{}>".format(str(value_type)))
        sl_node_ptr_type = sl_node_type.pointer()

        i = 0
        p = self.__val["head_node"]["next"]
        while p != self.__val["head_node"].address:
            p_to_node = p.cast(sl_node_ptr_type)
            yield "[{}]".format(i), p_to_node.dereference()
            i += 1
            p = p["next"]

    def children(self):
        for e in self.head():
            yield e

        for e in self.each():
            yield e


@register_printer("^kerbal::container::single_list<.*,.*>$")
class SingleListPrinter(ContainerRebindAllocatorOverloadPrinter, SingleListAllocatorUnrelatedPrinter):

    def __init__(self, val: gdb.Value):
        ContainerRebindAllocatorOverloadPrinter.__init__(self, val)
        SingleListAllocatorUnrelatedPrinter.__init__(self, val)

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
