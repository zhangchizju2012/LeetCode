#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 22:52:33 2017

@author: zhangchi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        stack = []
        temp = []
        if root is not None:
            stack.append(root)
        while len(stack) > 0:
            value = []
            for item in stack:
                value.append(item.val)
                if item.left is not None:
                    temp.append(item.left)
                if item.right is not None:
                    temp.append(item.right)
            stack = temp
            result.append(sum(value)*1.0/len(value))
            temp = []
        return result