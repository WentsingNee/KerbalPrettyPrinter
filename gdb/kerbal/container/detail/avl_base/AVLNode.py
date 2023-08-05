#
# @file       AVLNodePrinter.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb

from kerbal.check_gdb_val_type import check_gdb_val_type
from kerbal.register_class import register_class


def is_avl_vnull_node(p):
    return p["height"] == 0

def is_avl_null_node(p):
    return not p or is_avl_vnull_node(p)


def leftest_offspring(p):
    while not is_avl_null_node(p["left"]):
        print("left")
        p = p["left"]
    return p


# @register_class("kerbal::container::detail::avl_head_node")
class AVLHeadNode:

    @check_gdb_val_type("kerbal::container::detail::avl_head_node")
    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.val = val

    @staticmethod
    def get_printer(val):
        return AVLHeadNodePrinter(val)


class AVLHeadNodePrinter(AVLHeadNode):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        super().__init__(val)

    def dump(self):
        d = [
            ("left", self.val["left"]),
        ]
        return d

    def children(self):
        return self.dump()


# @register_class("kerbal::container::detail::avl_node_base")
class AVLNodeBase:

    @check_gdb_val_type("kerbal::container::detail::avl_node_base")
    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.val = val

    @staticmethod
    def get_printer(val):
        # if is_avl_vnull_node(val):
        #     return AVLVNULLNodePrinter(val)
        # else:
        #     return AVLNodeBasePrinter(val)
        return AVLNodeBasePrinter(val)


class AVLVNULLNodePrinter(AVLNodeBase):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        super().__init__(val)

    def dump(self):
        d = [
            ("aka", "VNULL"),
        ]
        return d

    def children(self):
        return self.dump()

    # def to_string(self):
    #     return "VNULL"

class AVLNodeBasePrinter(AVLNodeBase):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        super().__init__(val)

    def dump(self):
        d = [
            ("left", self.val["left"]),
            ("parent", self.val["parent"]),
            ("right", self.val["right"]),
            ("height", self.val["height"]),
        ]
        return d

    def children(self):
        return self.dump()
