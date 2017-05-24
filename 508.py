#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:46:59 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.result = {}
        self.helper(root)
        final = []
        maxValue = -float('inf')
        for item in self.result:
            if self.result[item] > maxValue:
                maxValue = self.result[item]
                final = [item]
            elif self.result[item] == maxValue:
                final.append(item)
        return final
    
    def helper(self, node):
        if node.left is not None:
            left = self.helper(node.left)
        else:
            left = 0
        if node.right is not None:
            right = self.helper(node.right)
        else:
            right = 0
        temp = left + right + node.val
        if temp in self.result:
            self.result[temp] += 1
        else:
            self.result[temp] = 1
        return temp
        
s = Solution()
node = TreeNode(5)
node.left = TreeNode(2)
node.right = TreeNode(-3)
print s.findFrequentTreeSum(node)