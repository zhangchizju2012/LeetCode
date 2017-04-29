#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 17:13:47 2017

@author: zhangchi
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islandList = {}
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    islandList[(i,j)] = 1
        
        result = 0
        tempList = []
        while len(islandList) > 0:
            result += 1
            tempList.append(islandList.popitem()[0])
            while len(tempList) > 0:
                temp = tempList.pop()
                try:
                    if (temp[0]-1,temp[1]) in islandList:
                        tempList.append((temp[0]-1,temp[1]))
                        islandList.pop((temp[0]-1,temp[1]))
                except:
                    pass
                try:
                    if (temp[0]+1,temp[1]) in islandList:
                        tempList.append((temp[0]+1,temp[1]))
                        islandList.pop((temp[0]+1,temp[1]))
                except:
                    pass
                try:
                    if (temp[0],temp[1]-1) in islandList:
                        tempList.append((temp[0],temp[1]-1))
                        islandList.pop((temp[0],temp[1]-1))
                except:
                    pass
                try:
                    if (temp[0],temp[1]+1) in islandList:
                        tempList.append((temp[0],temp[1]+1))
                        islandList.pop((temp[0],temp[1]+1))
                except:
                    pass
        return result
        
s = Solution()
print s.numIslands(["11110","11010","11000","00000"])

#==============================================================================
# can be improved by using hash table
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         islandList = []
#         row = len(grid)
#         if row == 0:
#             return 0
#         col = len(grid[0])
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == '1':
#                     islandList.append((i,j))
#         
#         result = 0
#         tempList = []
#         while len(islandList) > 0:
#             result += 1
#             tempList.append(islandList.pop())
#             while len(tempList) > 0:
#                 temp = tempList.pop()
#                 try:
#                     if (temp[0]-1,temp[1]) in islandList:
#                         tempList.append((temp[0]-1,temp[1]))
#                         islandList.remove((temp[0]-1,temp[1]))
#                 except:
#                     pass
#                 try:
#                     if (temp[0]+1,temp[1]) in islandList:
#                         tempList.append((temp[0]+1,temp[1]))
#                         islandList.remove((temp[0]+1,temp[1]))
#                 except:
#                     pass
#                 try:
#                     if (temp[0],temp[1]-1) in islandList:
#                         tempList.append((temp[0],temp[1]-1))
#                         islandList.remove((temp[0],temp[1]-1))
#                 except:
#                     pass
#                 try:
#                     if (temp[0],temp[1]+1) in islandList:
#                         tempList.append((temp[0],temp[1]+1))
#                         islandList.remove((temp[0],temp[1]+1))
#                 except:
#                     pass
#         return result
# 
#==============================================================================

#==============================================================================
# can be improved by 上一个方法
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         islandList = []
#         row = len(grid)
#         col = len(grid[0])
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == '1':
#                     islandList.append((i,j))
#         
#         result = 0
#         tempList = []
#         while len(islandList) > 0:
#             result += 1
#             tempList.append(islandList.pop())
#             while len(tempList) > 0:
#                 temp = tempList.pop()
#                 try:
#                     if grid[temp[0]-1][temp[1]] == '1':
#                         tempList.append((temp[0]-1,temp[1]))
#                         islandList.remove((temp[0]-1,temp[1]))
#                 except:
#                     pass
#                 try:
#                     if grid[temp[0]+1][temp[1]] == '1':
#                         tempList.append((temp[0]+1,temp[1]))
#                         islandList.remove((temp[0]+1,temp[1]))
#                 except:
#                     pass
#                 try:
#                     if grid[temp[0]][temp[1]-1] == '1':
#                         tempList.append((temp[0],temp[1]-1))
#                         islandList.remove((temp[0],temp[1]-1))
#                 except:
#                     pass
#                 try:
#                     if grid[temp[0]][temp[1]+1] == '1':
#                         tempList.append((temp[0],temp[1]+1))
#                         islandList.remove((temp[0],temp[1]+1))
#                 except:
#                     pass
#         return result
#==============================================================================
