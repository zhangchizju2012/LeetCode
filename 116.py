#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:34:33 2017

@author: zhangchi
"""

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        stack = []
        if root is not None:
            stack.append(root)
            while len(stack) > 0:
                temp = []
                for i in range(len(stack)):
                    item = stack[i]
                    if i != len(stack) - 1:
                        item.next = stack[i+1]
                    if item.left is not None:
                        temp.append(item.left)
                    if item.right is not None:
                        temp.append(item.right)
                stack = temp
            #return root
            
s = Solution()
n = TreeLinkNode(1)
n.left = TreeLinkNode(2)
n.right = TreeLinkNode(3)
n.left.left = TreeLinkNode(4)
n.left.right = TreeLinkNode(5)
n.right.left = TreeLinkNode(6)
n.right.right = TreeLinkNode(7)
result = s.connect(n)
                