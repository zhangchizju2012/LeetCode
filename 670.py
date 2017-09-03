#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:01:39 2017

@author: zhangchi
"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        origin = num
        dic = {}
        for i in xrange(10):
            dic[i] = []
        numberList = []
        index = 0
        while num != 0:
            numberList.append(num%10)
            dic[num%10].append(index)
            index += 1
            num = num // 10
        changed = sorted(numberList) # 与排序之后的比，找第一个不一样的
        if changed == numberList: # 说明已经排好序
            return origin
        else:    
            for i in xrange(len(changed)-1,-1,-1):
                if changed[i] == numberList[i]:
                    value = changed[i]
                    dic[value].pop() #似乎不需要
                else:
                    value = changed[i]
                    index = dic[value][0]
                    break
            numberList[i], numberList[index] = numberList[index], numberList[i]
            result = 0
            count = 1
            for item in numberList:
                result += count * item
                count *= 10
            return result
    
s = Solution()
print s.maximumSwap(9973)