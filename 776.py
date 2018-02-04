#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:07:54 2018

@author: zhangchi
"""

# 先复习一下怎么在二叉搜索树中删除一个节点吧

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        nodeStartMove = self.locate(root, V)
    
    def locate(self, node, V):
        if node.val == V:
            return node
        elif node.val > V:
            return self.locate(node.left, V)
        else:
            
        
# =============================================================================
#         node = root
#         if node.val == V:
#             right = node.right
#             node.right = None
#             return [node, right]
#         elif node.val > V:
#             node = node.left
# =============================================================================
            