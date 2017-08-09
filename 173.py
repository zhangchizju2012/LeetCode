#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:57:26 2017

@author: zhangchi
"""

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.history = []
        #self.direction = ["any thing does not matter"]#只是想让它长度和history相同
        if root is not None:
            self.history.append(root)
            while root.left is not None:
                self.history.append(root.left)
                #self.direction.append("left")
                root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.history) != 0

    def next(self):
        """
        :rtype: int
        """
        #dire = self.direction.pop()
        node = self.history.pop()
        value = node.val
        #if dire == "left" or len(self.history) == 0:
        # 后面==0很重要，说明结束了左边，要去右边了（包括到了右边的子树，也存在这样的问题（要去右子树的右子树））
        if node.right is not None:
            self.history.append(node.right)
            #self.direction.append("right")
            node = node.right
            while node.left is not None:
                self.history.append(node.left)
                #self.direction.append("left")
                node = node.left
        return value
        
node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(8)
node.left.right = TreeNode(4)
node.right.left = TreeNode(6)
node.right.right = TreeNode(9)
s = BSTIterator(node)
            
# [41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]

#==============================================================================
# class BSTIterator(object):
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.history = []
#         self.direction = ["any thing does not matter"]#只是想让它长度和history相同
#         if root is not None:
#             self.history.append(root)
#             while root.left is not None:
#                 self.history.append(root.left)
#                 self.direction.append("left")
#                 root = root.left
# 
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return len(self.history) != 0
# 
#     def next(self):
#         """
#         :rtype: int
#         """
#         dire = self.direction.pop()
#         node = self.history.pop()
#         value = node.val
#         if dire == "left" or len(self.history) == 0:
#         # 后面==0很重要，说明结束了左边，要去右边了（包括到了右边的子树，也存在这样的问题（要去右子树的右子树））
#             if node.right is not None:
#                 self.history.append(node.right)
#                 self.direction.append("right")
#                 node = node.right
#                 while node.left is not None:
#                     self.history.append(node.left)
#                     self.direction.append("left")
#                     node = node.left
#         return value
#==============================================================================
