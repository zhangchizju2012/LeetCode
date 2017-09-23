#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 19:53:15 2017

@author: zhangchi
"""

def longestPhrasesInATweet(array, k):
    temp = 0
    label = False
    length = len(array)
    for i, item in enumerate(array):
        temp += item
        if temp > k:
            index = i
            label = True
            break
    if label is False:
        return length
    else:
        result = [index] # result里的第i个里存的是从第i个元素开始的最长可能
        for i in xrange(length):
            temp -= array[i] # 去掉前一个
            while temp <= k:
                index += 1
                if index < length:
                    temp += array[index]
                else:
                    result.append(index-i-1)
                    return result
            result.append(index-i-1)
    
a = [1,2,3]
b = 4
print longestPhrasesInATweet(a,b)