"""
生成多对一的map数据，之后通过自动收集人为处理的方式生成map字典
"""

import csv
import os
import random


def gen_map_data():
    y_list = ['A', 'B', 'C', 'D']
    x_list = random.randint(1, 10)
    print(x_list)


def record_map():
    pass


if __name__ == '__main__':
    gen_map_data()

