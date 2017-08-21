#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 00:20:08 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 这个算法也适用于有个排好序的list,有两个元素被调换了顺序，找到这两个元素
    # 整个list返回来，一个一个扫描过去，找到下降的那个（别用sort）先用这种算法试试
    # 思路：第一个找上升的，第二个找下降的 （其实自己基本已经想好了）
    def __init__(self):
        self.prev = TreeNode(-float('inf')) # 用来储存前一个节点
        self.first = None
        self.second = None
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def helper(self, root):
        if root is None:
            return 
        else:
            self.helper(root.left)
            if self.first is None and root.val < self.prev.val:
                self.first = self.prev
            if self.first is not None and root.val < self.prev.val:
                self.second = root
            self.prev = root
            self.helper(root.right)
                
# =============================================================================
#     # 整个list返回来，一个一个扫描过去，找到下降的那个（别用sort）先用这种算法试试
#     # 只用helper返回一个值
#     # using O(n) space
#     def recoverTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: void Do not return anything, modify root in-place instead.
#         """
#         self.dic = {}
#         result = self.helper(root)
#         changed = sorted(result)
#         temp = []
#         for a,b in zip(result, changed):
#             if a!= b:
#                 temp.append(a)
#         self.dic[temp[0]].val, self.dic[temp[1]].val = self.dic[temp[1]].val, self.dic[temp[0]].val
#     
#     def helper(self, node):
#         if node.left is not None:
#             left = self.helper(node.left)
#         else:
#             left = []
#         if node.right is not None:
#             right = self.helper(node.right)
#         else:
#             right = []
#         self.dic[node.val] = node
#         return left + [node.val] + right
# =============================================================================
    
# =============================================================================
#     def recoverTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: void Do not return anything, modify root in-place instead.
#         """
#         if root is None:
#             return []
#         else:
#             return self.helper(root)
#     
#     def helper(self, node):
#         if node.left is not None:
#             left = self.helper(node.left)
#         else:
#             left = []
#         if node.right is not None:
#             right = self.helper(node.right)
#         else:
#             right = []
#         return left + [node.val] + right
# =============================================================================
