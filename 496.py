#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:01:57 2017

@author: zhangchi
"""

class Solution(object):
    # 完全自己想的，O(n)复杂度，其他更高复杂度的很容易想
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # 主要是对nums的操作，对findNums的操作只是最后对dict的查询而已，很弱智
        stack = [float('inf')] # 保证之后temp[-1]的正常运行，用来储存暂时未找到下个最大的元素，且他一定是从大到小排列的
        dic = {}
        for item in nums:
            while item > stack[-1]:
                dic[stack.pop()] = item # 比item小的元素可以一个一个建立dict，可以利用stack,从小到大把元素pop出来，直到碰到比自己大的元素
            stack.append(item) # 把自己放到stack最后，等待后面比自己大的元素，然后那个时候再pop出来
        for i in xrange(1,len(stack)):
            dic[stack[i]] = -1
        result = []
        for item in findNums:
            result.append(dic[item])
        return result
        
s = Solution()
print s.nextGreaterElement([2,4], [1,2,3,4])
        