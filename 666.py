#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:36:42 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # build tree
        node = self.buildTree(nums)
        path = self.getAllPath(node)
        return sum([sum(item) for item in path])
    
    def buildTree(self, nums):
        # build tree
        node = TreeNode(nums[0]%10)
        for i in xrange(1,len(nums)):
            value = nums[i]%10
            level = nums[i] // 100
            position = nums[i] % 100 // 10
            position -= 1
            temp = node
            # position可以看成二进制来处理
            for i in xrange(level-2,-1,-1):
                if i > 0:
                    if position & (2 ** i) > 0:
                        temp = temp.right
                    else:
                        temp = temp.left
                else:
                    if position & (2 ** i) == 1:
                        temp.right = TreeNode(value)
                    else:
                        temp.left = TreeNode(value)
        return node
    
    def getAllPath(self, node):
        if node.left is None and node.right is None:
            return [[node.val]]
        result = []
        if node.left is not None:
            result += self.getAllPath(node.left)
        if node.right is not None:
            result += self.getAllPath(node.right)
        return [[node.val]+item for item in result]
            
    
s = Solution()
result = s.pathSum([113, 221,331,342])