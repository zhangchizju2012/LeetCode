#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 19:50:55 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            # 找每一层最右边的和最左边的
            nodeList = [root]
            directionList = [[]]
            result = 1
            while len(nodeList) > 0:
                tempNodeList = []
                tempDirectionList = []
                for node, dire in zip(nodeList,directionList):
                    if node.left is not None:
                        tempNodeList.append(node.left)
                        tempDirectionList.append(dire+['left'])
                    if node.right is not None:
                        tempNodeList.append(node.right)
                        tempDirectionList.append(dire+['right'])
                # 找每一层最右边的和最左边的
                left = self.updateResult(directionList[0])
                right = self.updateResult(directionList[-1])
                result = max(result,right-left+1)
                nodeList = tempNodeList
                directionList = tempDirectionList
            return result
                        
    def updateResult(self,directionList):
        now = 1
        for item in directionList:
            if item == 'right':
                now = now * 2
            else:
                now = now * 2 - 1
        return now
    
s = Solution()
node = TreeNode(1)
node.left = TreeNode(3)
node.left.left = TreeNode(3)
node.left.left.left = TreeNode(6)
#node.left.right = TreeNode(3)
node.right = TreeNode(2)
node.right.right = TreeNode(9)
node.right.right.right = TreeNode(9)
node.right.right.right.right = TreeNode(9)
print s.widthOfBinaryTree(node)
# [1,1,1,1,1,1,1,null,null,null,1,null,null,null,null,2,2,2,2,2,2,2,null,2,null,null,2,null,2]