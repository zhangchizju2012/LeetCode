#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:34:22 2017

@author: zhangchi
"""
def combine(array):
    result = []
    for item in array:
        label_1 = False
        label_2 = False
        for index, dic in enumerate(result):
            if item[0] in dic:
                dic.add(item[1])
                label_1 = True
                index_1 = index
            elif item[1] in dic:
                dic.add(item[0])
                label_2 = True
                index_2 = index
        if label_1 is True and label_2 is True:
            if index_1 < index_2:
                dic_2 = result.pop(index_2)
                dic_1 = result.pop(index_1)
            else:
                dic_1 = result.pop(index_1)
                dic_2 = result.pop(index_2)
            result.append(dic_1.union(dic_2))
        if label_1 is False and label_2 is False:
            result.append(set([item[0],item[1]]))
    return [list(item) for item in result]

def combine_origin(array):
    result = []
    for item in array:
        label = False
        for dic in result:
            if item[0] in dic:
                dic.add(item[1])
                label = True
                break
            elif item[1] in dic:
                dic.add(item[0])
                label = True
                break
        if label is False:
            result.append(set([item[0],item[1]]))
    return [list(item) for item in result]

array = [['a','b'],['b','c'],['e','h'],['h','i'],['i','c']]
print combine(array)
"""

# 给一个文件，格式是这样的每行两个元素，你可以当字符串
# 要做的事情是对这个文件里元素进行分组，规则是只要两行中有相同的元素，那这两行中的元素都是一组的
# (A,B）(B,C) (E,F) (C,H) --> (A,B,C,H) (E,F)

def combine(array):
    result = []
    for item in array:
        label = False
        for dic in result:
            if item[0] in dic:
                dic.add(item[1])
                label = True
                break
            elif item[1] in dic:
                dic.add(item[0])
                label = True
                break
        if label is False:
            result.append(set([item[0],item[1]]))
    return [list(item) for item in result]



# 有M个苹果需要分到N个盘子里 写程序输出所有的分法，注意盘子是可以为空的，
# 另外(1,2,3)这种分发和（3，2，1）这种分发是重复的

def divide(m, n):
    if n == 1:
        return [[m]]
    else:
        result = []
        for i in xrange(m//n+1):
            temp = divide(m-i, n-1)
            for item in temp:
                if i <= item[0]:
                    result.append([i] + item)
        return result
        
        
        

def divide_origin(m, n):
    if n == 1:
        return [[m]]
    else:
        result = set()
        for i in xrange(m//n+1):
            temp = divide(m-i, n-1)
            for item in temp:
                addItem = tuple(sorted(item + [i]))
                if addItem not in result:
                    result.add(addItem)
        returnResult = []
        for item in result:
            returnResult.append(list(item))
        return returnResult
"""
    