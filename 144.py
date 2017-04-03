#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:16:59 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            temp = []
            temp.append(root)
            result = []
            while len(temp) > 0:
                point = temp.pop()
                result.append(point.val)
                if point.right is not None:
                    temp.append(point.right)
                if point.left is not None:
                    temp.append(point.left)
            return result
                