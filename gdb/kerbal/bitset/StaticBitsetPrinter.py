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

from kerbal.register_printer import kerbal_printer


@kerbal_printer.register_template_printer("^kerbal::bitset::static_bitset<.*,.*>$")
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

    @staticmethod
    def f(block, block_width):
        r = ""
        for i in range(block_width):
            for j in range(8):
                index = i * 8 + j
                if (block >> index) & 1 == 0:
                    r += '0'
                else:
                    r += '1'
            r += ' '
        return r

    def each(self):
        block_width = self.block_type().sizeof
        for i in range(self.block_size()):
            l = i * block_width * 8
            r = (i + 1) * block_width * 8
            x = self.f(self.__val["k_block"][i], block_width)
            yield f"[{i}] [{l}, {r}) : {x}", 0

    def children(self):
        yield "size", self.size()
        yield "block size", self.block_size()
        for e in self.each():
            yield e
