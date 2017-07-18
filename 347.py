#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:23:00 2017

@author: zhangchi
"""

class Solution(object):
    # 复杂度是n， 自己写的
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        dic = {}
        for item in nums:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
        temp = {}
        for item in dic:
            if dic[item] not in temp:
                temp[dic[item]] = [item]
            else:
                temp[dic[item]].append(item)
        result = []
        length = len(nums)
        # 可能的频率一个一个扫描过去
        for i in xrange(length,0,-1):
            if i in temp:
                result += temp[i]
                k -= len(temp[i])
                if k == 0:
                    return result
            
s = Solution()
print s.topKFrequent([1,1,1,2,2,3,3,4],2)