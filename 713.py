#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 20:38:21 2017

@author: zhangchi
"""

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        temp = []
        result = []
        now = 1
        for index, item in enumerate(nums):
            #if now * item < k:
            temp.append(index)
            now *= item
            if now >= k:
                if len(result) == 0 or (len(temp) > 1 and temp[-2] > result[-1][-1]):
                    # 同样index结尾的只留一个
                    t = list(temp)
                    t.pop()
                    result.append(t)
                while now >= k:
                    now = now / nums[temp[0]]
                    temp.pop(0)
        if len(result) == 0 or (len(temp) > 1 and temp[-2] > result[-1][-1]):
            result.append(list(temp))
            
        return result
            
        resultSet = set()
        for item in result:
            for i in xrange(len(item)):
                for j in xrange(i+1,len(item)+1):
                    resultSet.add(tuple(item[i:j]))
        return len(resultSet)
    
s = Solution()
print s.numSubarrayProductLessThanK([10, 5, 2, 1, 6],100)
#print s.numSubarrayProductLessThanK([4,4,2],1)
                