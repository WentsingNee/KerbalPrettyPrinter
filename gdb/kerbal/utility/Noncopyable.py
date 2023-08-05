#
# @file       Noncopyable.py
# @brief
# @date       2020-04-11
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

from kerbal.register_class import register_class


@register_class("kerbal::utility::noncopyconstructible")
class Noncopyconstructible:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    @staticmethod
    def get_printer(val):
        return NoncopyconstructiblePrinter(val)


class NoncopyconstructiblePrinter(Noncopyconstructible):

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        Noncopyconstructible.__init__(self, val)

    @staticmethod
    def to_string():
        return ""


@register_class("kerbal::utility::noncopyassignable")
class Noncopyassignable:

    def __init__(self, val):
        """
        @param val: gdb.Value
        """
        self.__val = val

    @staticmethod
    def get_printer(val):
        return NoncopyconstructiblePrinter(val)


class NoncopyassignablePrinter(Noncopyassignable):

    @staticmethod
    def to_string():
        return ""


@register_class("kerbal::utility::noncopyable")
class Noncopyable:

    @staticmethod
    def get_printer(val):
        return NoncopyconstructiblePrinter(val)


@register_class("kerbal::utility::noncopyable")
class NoncopyablePrinter(Noncopyable):

    @staticmethod
    def to_string():
        return ""
