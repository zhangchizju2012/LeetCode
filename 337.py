#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 10:17:01 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution(object):
    # dp
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.dic1 = {}
        self.dic2 = {}
        return max(self.helper1(root),self.helper2(root))
    
    def helper1(self, node):
        # helper1返回含有根的最大值
        if node not in self.dic1:
            temp = node.val
            if node.left is not None:
                temp += max(self.helper2(node.left),0)
            if node.right is not None:
                temp += max(self.helper2(node.right),0)
            self.dic1[node] = temp
        return self.dic1[node]
        
    
    def helper2(self, node):
        # helper2返回不含有根的最大值
        if node not in self.dic2:
            temp = 0
            if node.left is not None:
                temp += max(self.helper1(node.left),self.helper2(node.left),0)
            if node.right is not None:
                temp += max(self.helper1(node.right),self.helper2(node.right),0)
            self.dic2[node] = temp
        return self.dic2[node]


#==============================================================================
# class Solution(object):
#     # 没放字典里存储，很慢
#     def rob(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0
#         return max(self.helper1(root),self.helper2(root))
#     
#     def helper1(self, node):
#         # helper1返回含有根的最大值
#         temp = node.val
#         if node.left is not None:
#             temp += max(self.helper2(node.left),0)
#         if node.right is not None:
#             temp += max(self.helper2(node.right),0)
#         return temp
#         
#     
#     def helper2(self, node):
#         # helper2返回不含有根的最大值
#         temp = 0
#         if node.left is not None:
#             temp += max(self.helper1(node.left),self.helper2(node.left),0)
#         if node.right is not None:
#             temp += max(self.helper1(node.right),self.helper2(node.right),0)
#         return temp
#==============================================================================
        
        