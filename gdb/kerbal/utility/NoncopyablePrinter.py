#
# @file       NoncopyablePrinter.py
# @brief
# @date       2020-04-11
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import gdb

from kerbal.register_printer import register_printer


@register_printer("kerbal::utility::noncopyconstructible")
class NoncopyconstructiblePrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    @staticmethod
    def to_string():
        return ""


@register_printer("kerbal::utility::noncopyassignable")
class NoncopyassignablePrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    @staticmethod
    def to_string():
        return ""


@register_printer("kerbal::utility::noncopyable")
class NoncopyablePrinter:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    @staticmethod
    def to_string():
        return ""

