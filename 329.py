#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:14:11 2017

@author: zhangchi
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        temp = {}
        dic = {}
        row = len(matrix)
        if row == 0:
            return 0
        lenght= len(matrix[0])
        if lenght == 0:
            return 0
        # 方便查询，并且延伸一层，避免之后大量的if else
        for i in xrange(row):
            for j in xrange(lenght):
                temp[(i,j)] = matrix[i][j]
                dic[(i,j)] = 1
        # 延伸一层并置为X，避免之后大量的if else
        for i in xrange(-1,row+1):
            temp[(i,-1)] = float('inf')
            temp[(i,lenght)] = float('inf')
        for i in xrange(lenght):
            temp[(-1,i)] = float('inf')
            temp[(row,i)] = float('inf')
        
        result = 0
        count = row * lenght
        while count > 0:
            # 找到局部最小点
            result += 1
            remove = []
            for (i,j) in dic:
                if temp[(i,j)] <= min(temp[(i-1,j)],temp[(i+1,j)],temp[(i,j-1)],temp[(i,j+1)]):
                    remove.append((i,j))
            for item in remove:
                count -= 1
                temp[item] = float('inf')
                dic.pop(item)

        return result

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        temp = {}
        row = len(matrix)
        if row == 0:
            return 0
        lenght= len(matrix[0])
        if lenght == 0:
            return 0
        # 方便查询，并且延伸一层，避免之后大量的if else
        for i in xrange(row):
            for j in xrange(lenght):
                temp[(i,j)] = matrix[i][j]
        # 延伸一层并置为X，避免之后大量的if else
        for i in xrange(-1,row+1):
            temp[(i,-1)] = float('inf')
            temp[(i,lenght)] = float('inf')
        for i in xrange(lenght):
            temp[(-1,i)] = float('inf')
            temp[(row,i)] = float('inf')
        
        result = 0
        count = row * lenght
        while count > 0:
            # 找到局部最小点
            result += 1
            remove = []
            for i in xrange(row):
                for j in xrange(lenght):
                    if temp[(i,j)] == float('inf'):
                        continue
                    if temp[(i,j)] <= min(temp[(i-1,j)],temp[(i+1,j)],temp[(i,j-1)],temp[(i,j+1)]):
                        remove.append((i,j))
            for item in remove:
                count -= 1
                temp[item] = float('inf')

        return result
#==============================================================================
# class Node(object):
#     def __init__(self,i,j):
#         self.position = (i,j)
#         self.previous = []
#         self.next = []
# 
# class Solution(object):
#     # 真正的 topological sort（加了图）
#     def longestIncreasingPath(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#         temp = {}
#         nodeDic = {}
#         row = len(matrix)
#         if row == 0:
#             return 0
#         lenght = len(matrix[0])
#         if lenght == 0:
#             return 0
#         # 方便查询，并且延伸一层，避免之后大量的if else
#         for i in xrange(row):
#             for j in xrange(lenght):
#                 temp[(i,j)] = matrix[i][j]
#                 nodeDic[(i,j)] = Node(i,j)
#         
#         # 建立Graph
#         for i in xrange(row):
#             for j in xrange(lenght):
#                 if (i-1,j) in temp and temp[(i-1,j)] > temp[(i,j)]:
#                     nodeDic[(i,j)].next.append(nodeDic[(i-1,j)])
#                     nodeDic[(i-1,j)].previous.append(nodeDic[(i,j)])
#                 if (i+1,j) in temp and temp[(i+1,j)] > temp[(i,j)]:
#                     nodeDic[(i,j)].next.append(nodeDic[(i+1,j)])
#                     nodeDic[(i+1,j)].previous.append(nodeDic[(i,j)])
#                 if (i,j-1) in temp and temp[(i,j-1)] > temp[(i,j)]:
#                     nodeDic[(i,j)].next.append(nodeDic[(i,j-1)])
#                     nodeDic[(i,j-1)].previous.append(nodeDic[(i,j)])
#                 if (i,j+1) in temp and temp[(i,j+1)] > temp[(i,j)]:
#                     nodeDic[(i,j)].next.append(nodeDic[(i,j+1)])
#                     nodeDic[(i,j+1)].previous.append(nodeDic[(i,j)])
#         # # topological sort
#         count = 0
#         searched = {}
#         while len(searched) < row * lenght:
#             stack = []
#             count += 1
#             for i in xrange(row):
#                 for j in xrange(lenght):
#                     if len(nodeDic[(i,j)].previous) == 0 and nodeDic[(i,j)] not in searched:
#                         stack.append(nodeDic[(i,j)])
#                         searched[nodeDic[(i,j)]] = 1
#             for item in stack:
#                 for node in item.next:
#                     node.previous.remove(item)
#         return count
#         
#     # topological sort
#     # DP的思想看起来也是可以的
#     # better topological sort: http://www.allenlipeng47.com/blog/index.php/2016/01/22/longest-increasing-path-in-a-matrix/
#     def longestIncreasingPath(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#         temp = {}
#         row = len(matrix)
#         if row == 0:
#             return 0
#         lenght= len(matrix[0])
#         if lenght == 0:
#             return 0
#         # 方便查询，并且延伸一层，避免之后大量的if else
#         for i in xrange(row):
#             for j in xrange(lenght):
#                 temp[(i,j)] = matrix[i][j]
#         # 延伸一层并置为X，避免之后大量的if else
#         for i in xrange(-1,row+1):
#             temp[(i,-1)] = float('inf')
#             temp[(i,lenght)] = float('inf')
#         for i in xrange(lenght):
#             temp[(-1,i)] = float('inf')
#             temp[(row,i)] = float('inf')
#         
#         from Queue import Queue
#         q = Queue()
#         dic = {}
#         # 找到局部最小点
#         for i in xrange(row):
#             for j in xrange(lenght):
#                 if temp[(i,j)] <= min(temp[(i-1,j)],temp[(i+1,j)],temp[(i,j-1)],temp[(i,j+1)]):
#                     q.put((i,j))
#                     dic[(i,j)] = 1
#         # 四周有点比自己大，往四周推进 （有点拓扑排序的意思在）
#         while q.empty() is False:
#             (a,b) = q.get()
#             value = temp[(a,b)]
#             count = dic[(a,b)]
#             if temp[(a-1,b)] > value and temp[(a-1,b)] != float('inf'):
#                 dic[(a-1,b)] = count + 1
#                 q.put((a-1,b))
#             if temp[(a+1,b)] > value and temp[(a+1,b)] != float('inf'):
#                 dic[(a+1,b)] = count + 1
#                 q.put((a+1,b))
#             if temp[(a,b-1)] > value and temp[(a,b-1)] != float('inf'):
#                 dic[(a,b-1)] = count + 1
#                 q.put((a,b-1))
#             if temp[(a,b+1)] > value and temp[(a,b+1)] != float('inf'):
#                 dic[(a,b+1)] = count + 1
#                 q.put((a,b+1))
#         return count
#==============================================================================
        
s = Solution()
print s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
#print s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
        