#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 20:16:19 2017

@author: zhangchi
"""

class Solution(object):
    # 只要看看最多的元素有几个就可以了，知道了几个就至少要(n + 1) * (maxValue - 1) + maxCount个空
    # 但是似乎缺少数学证明
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = {}
        for item in tasks:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        maxValue = -float('inf')
        maxCount = 0
        for item in dic:
            if dic[item] > maxValue:
                maxValue = dic[item]
                maxCount = 1
            elif dic[item] == maxValue:
                maxCount += 1
        temp = (n + 1) * (maxValue - 1) + maxCount
        return max(len(tasks),temp) 
        
s = Solution()
print s.leastInterval(['A','b'],2)