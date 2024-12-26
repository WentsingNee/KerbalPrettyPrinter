#
# @file       __init__.py
# @brief
# @date       2020-04-11
# @author     Peter
# @copyright
#      Peter of [ThinkSpirit Laboratory](http://thinkspirit.org/)
#   of [Nanjing University of Information Science & Technology](http://www.nuist.edu.cn/)
#   all rights reserved
#

import importlib
import pathlib


base_dir = pathlib.Path(__path__[0])

for printer_file in base_dir.rglob("*Printer.py"):

    relative = printer_file.relative_to(base_dir)
    module_name = str(relative)[:-3].replace('/', '.')

    importlib.import_module(f"{__name__}.{module_name}", package=__name__)

