#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 23:36:05 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.temp = []
        self.helper1(root)
        self.temp.sort(reverse=True)
        self.dic = {}
        total = 0
        previous = float('inf')
        for item in self.temp:
            if item < previous:
                self.dic[item] = total
                total += item
            elif item == previous:
                total += item
        self.helper2(root)
        return root
        
    def helper1(self, node):
        if node is not None:
            self.temp.append(node.val)
            self.helper1(node.left)
            self.helper1(node.right)
    
    def helper2(self, node):
        if node is not None:
            node.val += self.dic[node.val]
            self.helper2(node.left)
            self.helper2(node.right)
            
            
# =============================================================================
# class Solution(object):
#     def convertBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         self.temp = []
#         self.helper1(root)
#         self.temp.sort(reverse=True)
#         self.helper2(root)
#         return root
#         
#     def helper1(self, node):
#         if node is not None:
#             self.temp.append(node.val)
#             self.helper1(node.left)
#             self.helper1(node.right)
#     
#     def helper2(self, node):
#         if node is not None:
#             value = node.val
#             for item in self.temp:
#                 if item > value:
#                     node.val += item
#                 else:
#                     break
#             self.helper2(node.left)
#             self.helper2(node.right)
# =============================================================================
            