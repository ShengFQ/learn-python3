#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Python 中并没有直接称为“数组”的数据结构，但通常使用列表（list）来实现类似数组的功能。
# 下面是一些基本的 Python 列表（可视为数组）运算示例：


my_list = [1, 2, 3, 4, 5]

my_list2 = [3, 4, 5]

# 两个列表向加
print(my_list+my_list2)
# [1, 2, 3, 4, 5, 3, 4, 5]

# 两个列表相减 执行跑错
## print(my_list-my_list2)

# 列表乘法
print(my_list2*2)
# [3, 4, 5, 3, 4, 5]

# 使用 range 函数创建数值列表
num_list = list(range(5))  # 创建一个包含0到4的列表
print(num_list)
# 访问第一个元素
first_element = my_list[0]
print(first_element)
# 访问最后一个元素
last_element = my_list[-1]
print(last_element)

# 在末尾添加元素
my_list.append(6)
print(my_list)
# 在指定位置插入元素
my_list.insert(1, 100)
print(my_list)