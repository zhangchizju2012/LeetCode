#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:35:21 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, count):
        self.val = x
        self.count = count # the number of points in left bottom
        self.dup = 1
        self.left = None
        self.right = None


class Solution(object):
    # inspired by https://discuss.leetcode.com/topic/31405/9ms-short-java-bst-solution-get-answer-when-building-bst/2
    # write by myself
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        self.result = [0] * length
        node = None
        for i in range(length-1,-1,-1):
            node = self.insert(node,nums[i],0,i)
        return self.result
        
    def insert(self,node,value,count,position):
        if node is None:
            node = TreeNode(value,0)
            self.result[position] = count
        elif value == node.val:
            node.dup += 1
            self.result[position] = count + node.count
        elif value > node.val:
            node.right = self.insert(node.right,value,count+node.count+node.dup,position)
        else:
            node.count += 1
            node.left = self.insert(node.left,value,count,position)
        return node

s = Solution()
print s.countSmaller([3, 2, 2, 6, 1])

#==============================================================================
# class Solution(object):
#     # wrong
#     def countSmaller(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         length = len(nums)
#         result = [0] * length
#         for i in range(length-2,-1,-1):
#             temp = nums[i]
#             label = False
#             for j in range(i+1,length):
#                 if temp > nums[j]:
#                     result[i] = result[j] + 1
#                     label = True
#                     break
#                 elif temp == nums[j]:
#                     result[i] = result[j]
#                     label = True
#                     break
#             if label == False:
#                 result[i] = 0
#         return result
#==============================================================================
