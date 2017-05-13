#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:34:58 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root,"")
        final = [int(item) for item in self.result]
        return sum(final)
        
    def helper(self, root, temp):
        if root.left is None and root.right is None:
            self.result.append(temp+str(root.val))
        else:
            if root.left is not None:
                self.helper(root.left,temp+str(root.val))
            if root.right is not None:
                self.helper(root.right,temp+str(root.val))
                
s = Solution()
point = TreeNode(1)
point.left = TreeNode(2)
point.right = TreeNode(3)
print s.sumNumbers(point)