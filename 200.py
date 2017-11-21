#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Reviewed on Tue Nov 21 11:25:46 2017

@author: zhangchi
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        result = 0
        self.row = row = len(grid)
        if row == 0:
            return 0
        self.length = length = len(grid[0])
        for i in xrange(row):
            for j in xrange(length):
                if self.grid[i][j] == '1':
                    result += 1
                    self.search(i,j)
        return result
        
    
    def search(self, i, j):
        self.grid[i][j] = '2'
        if 0 <= i-1 < self.row and 0 <= j < self.length and self.grid[i-1][j] == '1':
            self.search(i-1,j)
        if 0 <= i+1 < self.row and 0 <= j < self.length and self.grid[i+1][j] == '1':
            self.search(i+1,j)
        if 0 <= i < self.row and 0 <= j-1 < self.length and self.grid[i][j-1] == '1':
            self.search(i,j-1)
        if 0 <= i < self.row and 0 <= j+1 < self.length and self.grid[i][j+1] == '1':
            self.search(i,j+1)


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
