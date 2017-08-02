#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:40:33 2017

@author: zhangchi
"""

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# 跟116很像，这个解法比116的好很多，116有两种解法，java一种python一种，都不太满足constant space这个要求其实
# 现在这个是constant space了
# 巧妙的利用next来扫描父节点，避免了116python解法中用stack来储存父节点（这是关键点）
# 然后只要用nextLevel来记录父节点的起点
# 看了一眼答案，自己写的（主要就是看到了利用next来扫描父节点这个思想）
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        node = TreeLinkNode(0) # 下一层的起点
        label = False
        while root is not None:
            if root.left is not None:
                node.next = root.left
                node = node.next
                if label is False:
                    nextLevel = root.left # 找到下一层的起点，用nextLevel来记录父节点的起点
                    label = True
            if root.right is not None:
                node.next = root.right
                node = node.next
                if label is False:
                    nextLevel = root.right
                    label = True
            root = root.next # 同层的父节点一个一个扫描过去
            if root is None: # 这一层的父节点扫描完了
                if label is True: # 还有下一层
                    root = nextLevel
                    node = TreeLinkNode(0)
                    label = False
            
        