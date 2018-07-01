#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 18:38:51 2018

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node(object):
    def __init__(self, x):
        self.val = x
        self.leftup = None
        self.leftdown = None
        self.rightup = None
        self.rightdown = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.dic = {}
        self.helper(root)
        node = self.dic[target]
        self.result = []
        self.helper2(node, '', K)
        return self.result
    
    def helper2(self, node, direction, distance):
        if distance == 0:
            self.result.append(node.val)
        else:
            if node.leftup is not None and direction != 'rightdown':
                self.helper2(node.leftup, 'leftup', distance-1)
            if node.leftdown is not None and direction != 'rightup':
                self.helper2(node.leftdown, 'leftdown', distance-1)
            if node.rightup is not None and direction != 'leftdown':
                self.helper2(node.rightup, 'rightup', distance-1)
            if node.rightdown is not None and direction != 'leftup':
                self.helper2(node.rightdown, 'rightdown', distance-1)
    
    def helper(self, node):
        newnode = Node(node.val)
        self.dic[node.val] = newnode
        if node.left is not None:
            leftnewnode = self.helper(node.left)
            newnode.leftdown = leftnewnode
            leftnewnode.rightup = newnode
        if node.right is not None:
            rightnewnode = self.helper(node.right)
            newnode.rightdown = rightnewnode
            rightnewnode.leftup = newnode
        return newnode
        
node = TreeNode(3)
node.left = TreeNode(5)
node.right = TreeNode(1)
node.left.left = TreeNode(6)
node.left.right = TreeNode(2)
node.left.right.left = TreeNode(7)
node.left.right.right = TreeNode(4)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)
s = Solution()
result = s.distanceK(node,5,2)