#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 15:10:55 2017

@author: zhangchi
"""

#==============================================================================
# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 
# class Solution(object):
#     def __init__(self):
#         self.result = []
#     def kthSmallest(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: int
#         """
#         self.helper(root)
#         return self.result[k-1]
#         
#     def helper(self, root):
#         if root is not None:
#             self.helper(root.left)
#             self.result.append(root.val)
#             self.helper(root.right)
# 
#==============================================================================

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        return self.helper(root)
        
    def helper(self, root):
        if root is not None:
            temp = self.helper(root.left)
            if temp is not None:
                return temp
            self.count += 1
            if self.count == self.k:
                return root.val
            temp = self.helper(root.right)
            if temp is not None:
                return temp
node = TreeNode(5)
node.left = TreeNode(3)
node.left.left = TreeNode(1)
node.right = TreeNode(7)
node.right.right = TreeNode(9)
s = Solution()
print s.kthSmallest(node,2)