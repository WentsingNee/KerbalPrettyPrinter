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

# from kerbal import lookup

import sys
import os
import re

ext_match = re.compile(R".*\.py$")

for root, path, files in os.walk(sys.path[0]):
    print(f"{root}   {path}   {files}")
    # for file in files:
    #     if not ext_match.match(file):
    #         continue
    #     print(f"{root}/{file}")
    #     # __import__(file)

# def traverse_dir(base, relative):
#     path = os.path.join(base, relative)
#     for file in os.listdir(path):
#         file_path = os.path.join(path, file)
#         if os.path.isdir(file_path):
#             print("文件夹：", file_path)
#             traverse_dir(base, file_path)
#             continue
#         print("文件：", file_path)
#         print("relative：", relative)
#         if not ext_match.match(file):
#             continue
#         # path
#         __import__(file)
#
# traverse_dir(sys.path[0], "")
