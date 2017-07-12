#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 01:28:54 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 查到左子树为空为止
    # 碰到left替换成right，之后再全补成left, 若是right全都pop出去，这样是全部扫描（慢）
    # 可以搞二分，直接从第一个到后面一个一个改成right，第一个改成right，
    # 到最底下节点依旧存在就说明最后一层的前面一半都是存在的，若不存在再把第一个改回left
    # 统计次数的时候有些位控制的感觉，每个位置的right代表的层数不一样
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.root = root
        if root is None:
            return 0
        trajectory = []
        count = 0
        temp = 1
        while root.left is not None:
            trajectory.append('left')
            count += temp
            temp *= 2
            root = root.left
        temp /= 2
        for i in xrange(len(trajectory)):
            trajectory[i] = 'right'
            if self.checkExist(trajectory) is False:
                trajectory[i] = 'left'
            else:
                count += temp
            temp /= 2
        return count + 1
            
    def checkExist(self, trajectory):
        node = self.root
        for item in trajectory:
            if item == "left":
                node = node.left
            else:
                node = node.right
        return node is not None

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)
s = Solution()
print s.countNodes(node)