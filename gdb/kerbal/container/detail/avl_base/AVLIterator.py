#
# @file       AVLIterator.py
# @brief
# @date       2023-08-04
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb

from kerbal.container.detail.avl_base.AVLNode import leftest_offspring


class AVLIter:

    def __init__(self, current):
        self.__current = current

    def inorder_next(self):
        avl_node_base_type = gdb.lookup_type("kerbal::container::detail::avl_node_base")

        current = self.__current
        if is_avl_null_node(current.cast(avl_node_base_type)["right"]):
            ancestor = current.cast(avl_node_base_type)["parent"]
            while current != ancestor["left"]:  # warning: head doesn't have right domain!
                # is parent's right son
                current = ancestor
                ancestor = current.cast(avl_node_base_type)["parent"]
            # is parent's left son
            current = ancestor
        else:
            current = leftest_offspring(current.cast(avl_node_base_type)["right"])
        return current

    def forward(self):
        self.__current = self.inorder_next()

    def dereference(self):
        return self.__current.dereference()

    def __eq__(self, rhs):
        return self.__current == rhs.current

    def __ne__(self, rhs):
        return self.__current != rhs.current
