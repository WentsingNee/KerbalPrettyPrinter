#
# @file       ArrayPrinter.py
# @brief
# @date       2021-08-25
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_printer import kerbal_printer


@kerbal_printer.register_template_printer("^kerbal::container::array<.*,.*>$")
class ArrayPrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def size(self):
        return self.__val["k_data"].type.range()[1] + 1

    def dump(self):
        d = dict(self.children())
        return d

    def __getitem__(self, i):
        return self.__val["k_data"][i]

    def each(self):
        for i in range(self.size()):
            yield f"[{i}]", self[i]

    def children(self):
        for e in self.each():
            yield e
