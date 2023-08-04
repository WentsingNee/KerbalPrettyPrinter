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


def is_avl_vnull_node(p):
    return not p or p["height"] == 0

def leftest_offspring(p):
    while not is_avl_vnull_node(p["left"]):
        p = p["left"]
    return p

class AVLIterator:

    def __init__(self, current):
        self.__current = current

    def inorder_next(self):
        node_base_type = gdb.lookup_type("kerbal::container::detail::avl_node_base")

        current = self.__current
        if is_avl_vnull_node(current.cast(node_base_type)["right"]):
            ancestor = current.cast(node_base_type)["parent"]
            print("if")
            print(current)
            print(ancestor.type)
            print(ancestor)
            # print(current != ancestor["left"])
            while current != ancestor["left"]: # warning: head doesn't have right domain!
                print("xxx")
                # is parent's right son
                current = ancestor
                ancestor = current.cast(node_base_type)["parent"]
            # is parent's left son
            current = ancestor
        else:
            print("else")
            current = leftest_offspring(current.cast(node_base_type)["right"])
        return current

    def forward(self):
        self.__current = self.inorder_next()

    def current(self):
        return self.__current

    def dereference(self):
        return self.__current.dereference()

    def __eq__(self, rhs):
        return self.__current == rhs.__current

    def __ne__(self, rhs):
        return self.__current != rhs.__current
