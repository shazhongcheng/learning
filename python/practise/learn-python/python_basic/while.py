#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    while.py
 @Function:    while definition
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/30
"""

"""一、循环结构的概述"""

"""
1、为什么需要循环结构？
    如果要打印1到10之间的所有自然数，你可能会这样实现：
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)
    print(10)
    如果要打印1到1000之间的所有自然数，你就要写1000行代码，而且这1000行代码都是重复的
    print语句，唯一的区别在于要打印的自然数不同
"""


"""
2、什么是循环结构？
    使用循环结构，上面的需求可以这样实现：
    i = 1
    while i < 11:
        print(i)
        i += 1
    或者这样实现：
    for i in range(1, 11):
        print(i)
    代码量少了很多，而且没有重复的代码
    如果要打印1到1000之间的所有自然数，只需要把11改为1001就可以了
    
    循环结构指的是：程序根据循环条件反复执行某段代码，直到不满足循环条件为止
    python提供了两种实现循环结构的语句：while语句和for-in语句
"""


"""二、while语句"""

"""
while语句的语法格式：
    初始化部分
    while 循环条件:
        循环体
    其中，循环体对应的代码块必须缩进
        (1) 初始化部分：用于设置循环的初始条件，比如循环控制变量的初始值
        (2) 循环条件：每次循环都要判断循环条件的布尔值，以决定继续循环还是终止循环
            循环条件中通常包含循环控制变量
        (3) 循环体：这是循环操作的主体内容，可以是一条语句，也可以是多条语句
            循环体中的某些语句用于改变循环控制变量的值，从而改变循环条件的布尔值

while语句的执行流程：
    执行完一次初始化部分之后，反复判断循环条件的布尔值
    如果循环条件的布尔值为False，则终止循环
    如果循环条件的布尔值为True，则执行循环体，执行完循环体后再次判断循环条件的布尔值
"""

i = 1
while i < 11:
    print(i)
    i += 1

"""
    应该确保让循环条件的布尔值在某一时刻变为False，以避免while语句陷入死循环(无限循环)，
    即永远不会终止的循环

    i = 1
    while True:
        print(i)
        i += 1
"""

"""
    有时候循环条件可能不太容易确定，需要在循环体中才能决定是否要退出循环，在这种情况下，
    可以使用while-True-break结构，也就是说，通过while True构造一个无限循环，
    在循环体中满足某个条件时通过break退出循环
"""

while True:
    word = input('请输入一个单词：')
    if not word:
        break
    print('输入的单词是:', word)