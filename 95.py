#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:37:44 2016

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def updateTree(self,value,tree):
        if tree is not None:
            temp = TreeNode(tree.val + value)
            temp.left = self.updateTree(value,tree.left)
            temp.right = self.updateTree(value,tree.right)
            return temp
    def helpTree(self,n,result):
        temp = []
        for i in range(n):
            if i in result:
                temp1 = result[i]
            else:
                temp1,result = self.helpTree(i,result)
                result[i] = temp1
            if n-1-i in result:
                temp2 = result[n-1-i]
            else:
                temp2,result = self.helpTree(n-1-i,result)
                result[n-1-i] = temp2
            if len(temp1) == 0:
                for item2 in temp2:
                    tempTree = TreeNode(i+1)
                    tempTree.left = None
                    tempTree.right = self.updateTree(i+1,item2)
                    temp.append(tempTree)
            elif len(temp2) == 0:
                for item1 in temp1:
                    tempTree = TreeNode(i+1)
                    tempTree.left = item1
                    tempTree.right = None
                    temp.append(tempTree)
            else:
                for item1 in temp1:
                    for item2 in temp2:
                        tempTree = TreeNode(i+1)
                        tempTree.left = item1
                        tempTree.right = self.updateTree(i+1,item2)
                        temp.append(tempTree)
        return temp,result
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 1:
            return [TreeNode(1)]
        dictionary = {0:[],1:[TreeNode(1)]}
        count,_ = self.helpTree(n,dictionary)
        return count
        
S = Solution()
a = S.generateTrees(5)