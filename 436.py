#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:13:00 2017

@author: zhangchi
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution(object):
    # 因为所有的start都是唯一的，所以可以按照start来建dict, 然后按start来排序，
    # 然后对于其中的某个item,只要看这个item的item[1]，然后后面的list的start与这个item[1]进行比较就行了
    # 找后面list的时候可以用binary search
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        self.dic = {}
        for index, item in enumerate(intervals):
            self.dic[item[0]] = index
        intervals.sort(key=lambda x:x[0])
        self.list = [item[0] for item in intervals]
        self.length = len(intervals)
        result = [0] * self.length
        for index, item in enumerate(intervals):
            result[self.dic[item[0]]] = self.helper(index+1,item[1])
        return result

    def helper(self, i, value):
        # binary search
        if i == self.length:
            return -1
        if self.list[i] >= value:
            return self.dic[self.list[i]]
        else:
            if self.list[-1] < value:
                return -1
            if self.list[-1] >= value and self.list[-2] < value:
                return self.dic[self.list[-1]]
            left = i
            right = self.length - 1
            middle = (left + right) // 2
            while True:
                if self.list[middle] >= value and self.list[middle-1] < value:
                    return self.dic[self.list[middle]]
                if self.list[middle] >= value and self.list[middle-1] >= value:
                    right = middle
                if self.list[middle] < value:
                    left = middle
                middle = (left + right) // 2
            
#==============================================================================
# 
# class Solution(object):
#     def findRightInterval(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[int]
#         """
#         self.dic = {}
#         for index, item in enumerate(intervals):
#             self.dic[item.start] = index
#         intervals.sort(key=lambda x:x.start)
#         self.list = [item.start for item in intervals]
#         self.length = len(intervals)
#         result = [0] * self.length
#         for index, item in enumerate(intervals):
#             result[self.dic[item.start]] = self.helper(index+1,item.end)
#         return result
# 
#     def helper(self, i, value):
#         if i == self.length:
#             return -1
#         if self.list[i] >= value:
#             return self.dic[self.list[i]]
#         else:
#             if self.list[-1] < value:
#                 return -1
#             else:
#                 for index in xrange(i,self.length):
#                     if self.list[index] > value:
#                         return self.dic[self.list[index]]
#==============================================================================
#==============================================================================
# class Solution(object):
#     def findRightInterval(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[int]
#         """
#         self.dic = {}
#         for index, item in enumerate(intervals):
#             self.dic[item[0]] = index
#         intervals.sort(key=lambda x:x[0])
#         self.list = [item[0] for item in intervals]
#         self.length = len(intervals)
#         result = [0] * self.length
#         for index, item in enumerate(intervals):
#             result[self.dic[item[0]]] = self.helper(index+1,item[1])
#         return result
# 
#     def helper(self, i, value):
#         if i == self.length:
#             return -1
#         if self.list[i] >= value:
#             return self.dic[self.list[i]]
#         else:
#             if self.list[-1] < value:
#                 return -1
#             else:
#                 for index in xrange(i,self.length):
#                     if self.list[index] >= value:
#                         return self.dic[self.list[index]]
#==============================================================================
                        
s = Solution()
print s.findRightInterval([ [1,4], [2,3], [3,4] ])