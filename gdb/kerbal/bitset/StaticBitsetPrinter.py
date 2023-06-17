#
# @file       StaticBitsetPrinter.py
# @brief
# @date       2021-08-27
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_printer import register_printer


@register_printer("^kerbal::bitset::static_bitset<.*,.*>$")
class StaticBitsetPrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    def size(self):
        return self.__val.type.template_argument(0)

    def block_size(self):
        return self.__val["k_block"].type.range()[1] + 1

    def block_type(self):
        return self.__val.type.template_argument(1)

    def f(self, x):
        r = str()
        for i in range(self.block_type().sizeof):
            for j in range(8):
                index = i * 8 + j
                if (x >> index) & 1 == 0:
                    r = r + '0'
                else:
                    r = r + '1'
            r = r + ' '
        return r

    def each(self):
        block_width = self.block_type().sizeof
        for i in range(self.block_size()):
            l = i * block_width * 8
            r = (i + 1) * block_width * 8
            x = self.f(self.__val["k_block"][i])
            yield "{} ~ {} : {}".format(l, r, x), x

    def children(self):
        yield "size: ", self.size()
        yield "block size: ", self.block_size()
        for e in self.each():
            yield e
