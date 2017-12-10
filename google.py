#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:01:57 2017

@author: zhangchi
"""

# Definition for a tree node.
class TreeNode(object):
    def __init__(self, x):
        self.label = x
        self.children = []
        
def preprocess(E):
    length = len(E)
    temp = []
    for i in xrange(length//2):
        if E[i*2] < E[i*2+1]:
            temp.append([E[i*2], E[i*2+1]])
        else:
            temp.append([E[i*2+1], E[i*2]])
    temp.sort(key=lambda x:x[0])
    result = []
    for item in temp:
        result += item
    return result

def buildTree(A,E):
    B = preprocess(E)
    dic = {}
    length = len(B) // 2
    for i in xrange(length):
        if B[i*2] in dic:
            nodeParent = dic[B[i*2]]
        else:
            nodeParent = TreeNode(A[B[i*2]-1])
            dic[B[i*2]] = nodeParent
            
        nodeChild = TreeNode(A[B[i*2+1]-1])
        dic[B[i*2+1]] = nodeChild
        nodeParent.children.append(nodeChild)
        
    return dic[B[0]]

class Solution(object):
    def longestUnivaluePath(self, node):
        if node is None:
            return 0
        self.result = 1
        self.helper(node)
        return self.result - 1
        
    def helper(self, node):
        count = 1
        childCountList = []
        for childNode in node.children:
            childCount, childLabel = self.helper(childNode)
            if childLabel == node.label:
                if len(childCountList) == 0:
                    childCountList.append(childCount)
                elif len(childCountList) == 1:
                    if childCount > childCountList[0]:
                        childCountList = [childCount] + childCountList
                    else:
                        childCountList.append(childCount)
                else:
                    if childCount > childCountList[0]:
                        childCountList = [childCount,childCountList[0]]
                    elif childCount > childCountList[1]:
                        childCountList[1] = childCount
        self.result = max(self.result, count+sum(childCountList))
        if len(childCountList) >= 1:
            return 1 + childCountList[0], node.label
        else:
            return 1, node.label
        
A = [1,1,1,2,2]
B = [1,2,1,3,2,4,2,5]
result = buildTree(A,B)
s = Solution()
print s.longestUnivaluePath(result)

# =============================================================================
# def buildTree(A,E):
#     B = preprocess(E)
#     dic = {}
#     index = 0
#     length = len(B) // 2
#     for i in xrange(length):
#         if B[i*2] in dic:
#             nodeParent = dic[B[i*2]]
#         else:
#             nodeParent = TreeNode(A[index])
#             dic[B[i*2]] = nodeParent
#             index += 1
#             
#         nodeChild = TreeNode(A[index])
#         dic[B[i*2+1]] = nodeChild
#         index += 1
#         nodeParent.children.append(nodeChild)
#         
#     return dic[B[0]]
# =============================================================================


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:57:32 2017

@author: zhangchi
"""
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

class TreeNode(object):
    def __init__(self, x):
        self.label = x
        self.children = []

def preprocess(E):
    length = len(E)
    temp = []
    for i in range(length//2):
        if E[i*2] < E[i*2+1]:
            temp.append([E[i*2], E[i*2+1]])
        else:
            temp.append([E[i*2+1], E[i*2]])
    #temp.sort(key=lambda x:x[0])
    result = []
    for item in temp:
        result += item
    return result

def buildTree(A,E):
    B = preprocess(E)
    dic = {}
    length = len(B) // 2
    for i in range(length):
        if B[i*2] in dic:
            nodeParent = dic[B[i*2]]
        else:
            nodeParent = TreeNode(A[B[i*2]-1])
            dic[B[i*2]] = nodeParent
        if B[i*2+1] in dic:
            nodeChild = dic[B[i*2+1]]
        else:
            nodeChild = TreeNode(A[B[i*2+1]-1])
            dic[B[i*2+1]] = nodeChild
        nodeParent.children.append(nodeChild)
    return dic[B[0]]

def solution(A, E):
    # write your code in Python 3.6
    if len(A) <= 1:
        return 0
    else:
        global result
        result = 1
        node = buildTree(A,E)
        helper(node)
        return result - 1
        
def helper(node):
    global result
    count = 1
    childCountList = []
    for childNode in node.children:
        childCount, childLabel = helper(childNode)
        if childLabel == node.label:
            if len(childCountList) == 0:
                childCountList.append(childCount)
            elif len(childCountList) == 1:
                if childCount > childCountList[0]:
                    childCountList = [childCount] + childCountList
                else:
                    childCountList.append(childCount)
            else:
                if childCount > childCountList[0]:
                    childCountList = [childCount, childCountList[0]]
                elif childCount > childCountList[1]:
                    childCountList[1] = childCount
    result = max(result, sum(childCountList) + count)
    if len(childCountList) >= 1:
        return 1 + childCountList[0], node.label
    else:
        return 1, node.label
    
    
    
    
A = [1,1,1,2,2]
B = [5,2,1,2,3,1,2,4]
print preprocess(B)
temp = buildTree(A,B)
print solution(A, B)
[[1, 2, 2, 1, 1,1,1,1,1,1], [1, 2, 1, 3, 1, 4, 4, 5,4,6,6,7,6,8,8,9,5,10]] 
[[5, 2, 2, 5, 5], [1, 2, 1, 3, 1, 4, 4, 5]] 
[[1, 1, 1, 2, 2], [2, 4, 2, 5, 2, 1, 1, 3]] 
[[1],[]]