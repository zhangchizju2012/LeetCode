#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 20:11:30 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        self.sum = 0
        self.set = {}
        self.helper(root)
        # 整个不能是subtree，主要是避免0之类的问题
        self.set[self.sum] -= 1
        if self.sum % 2 == 1:
            return False
        else:
            target = self.sum / 2
            if target in self.set and self.set[target] > 0:
                return True
            else:
                return False
    
    def helper(self, node):
        if node is None:
            return 0
        else:
            left = self.helper(node.left)
            right = self.helper(node.right)
            self.sum += node.val
            value = left + right + node.val
            # value是所有可能的subtree的和
            if value in self.set:
                self.set[value] += 1
            else:
                self.set[value] = 1
            return value
            
s = Solution()
node = TreeNode(5)
node.left = TreeNode(10)
node.right = TreeNode(10)
node.right.left = TreeNode(2)
node.right.right = TreeNode(3)
print s.checkEqualTree(node)