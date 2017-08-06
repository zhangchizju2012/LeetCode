#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:48:53 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        stack = [root]
        result = []
        label = True
        while label:
            label = False
            tempResult = []
            changedResult = []
            nextStack = []
            for item in stack:
                if item is None:
                    tempResult.append("")
                    nextStack.append(None)
                    nextStack.append(None)
                else:
                    tempResult.append(str(item.val))
                    if item.left is not None:
                        nextStack.append(item.left)
                        label = True
                    else:
                        nextStack.append(None)
                    if item.right is not None:
                        nextStack.append(item.right)
                        label = True
                    else:
                        nextStack.append(None)
                tempResult.append("")
            tempResult.pop()
            for eachResult in result:
                eachTempResult = [""]
                for item in eachResult:
                    eachTempResult.append(item)
                    eachTempResult.append("")
                changedResult.append(eachTempResult)
            changedResult.append(tempResult)
            if label:
                result = changedResult
                stack = nextStack
        return changedResult
        
        
s = Solution()
node = TreeNode(1)
node.left = TreeNode(2)
print s.printTree(node)
                    

        