#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 20:17:37 2017

@author: zhangchi
"""

class Solution(object):
    # 看了答案自己写的：https://discuss.leetcode.com/topic/22179/python-easy-to-understand-solution-divide-and-conquer
    # 相同结果的不一定是一个
    # 思路还是很简单的，每个遇到一个+/-/*，就把他们视为最后计算的，然后分成左右部分，然后recursion
    # 这题也是用recursion来正向思维
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.helper(input)
        
    def helper(self, s):
        result = []
        for i in xrange(len(s)):
            if s[i] in "+-*":
                left = self.helper(s[:i])
                right = self.helper(s[i+1:])
                for leftItem in left:
                    for rightItem in right:
                        if s[i] == "+":
                            result.append(leftItem+rightItem)
                        elif s[i] == "-":
                            result.append(leftItem-rightItem)
                        elif s[i] == "*":
                            result.append(leftItem*rightItem)
        if len(result) == 0: # result长度为0说明这个s只含有数字
            result.append(int(s))
        return result
        
s = Solution()
print s.diffWaysToCompute("2*3-4*5")

#==============================================================================
# class Solution(object):
#     # 相同结果的视为一个
#     def diffWaysToCompute(self, input):
#         """
#         :type input: str
#         :rtype: List[int]
#         """
#         return list(self.helper(input))
#         
#     def helper(self, s):
#         result = set()
#         for i in xrange(len(s)):
#             if s[i] in "+-*":
#                 left = self.helper(s[:i])
#                 right = self.helper(s[i+1:])
#                 for leftItem in left:
#                     for rightItem in right:
#                         if s[i] == "+":
#                             result.add(leftItem+rightItem)
#                         elif s[i] == "-":
#                             result.add(leftItem-rightItem)
#                         elif s[i] == "*":
#                             result.add(leftItem*rightItem)
#         if len(result) == 0:
#             result.add(int(s))
#         return result
#==============================================================================
