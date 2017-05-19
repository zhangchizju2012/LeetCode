#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:21:12 2017

@author: zhangchi
"""
class Solution(object):
    #思路：由一个点往外扩张出去
    # finish on the plane from Shanghai to Vancuvour
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        dic = {}
        # 只是为了避免在后面的while循环里不断地判断有没有超过界限，target相应加了2 * row + 2 * col
        for i in xrange(row):
            dic[(i,-1)] = float('inf')
            dic[(i,col)] = float('inf')
        for i in xrange(col):
            dic[(-1,i)] = float('inf')
            dic[(row,i)] = float('inf')
        target = row * col + 2 * row + 2 * col
        result = [[0] * col for _ in xrange(row)]
        nextTime = []
        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j] == 0:
                    dic[(i,j)] = 0
                    nextTime.append((i,j))
        count = 0
        while len(dic) < target:
            temp = []
            for (a,b) in nextTime:
                if (a-1,b) not in dic:
                    dic[(a-1,b)] = count + 1
                    temp.append((a-1,b))
                if (a+1,b) not in dic:
                    dic[(a+1,b)] = count + 1
                    temp.append((a+1,b))
                if (a,b-1) not in dic:
                    dic[(a,b-1)] = count + 1
                    temp.append((a,b-1))
                if (a,b+1) not in dic:
                    dic[(a,b+1)] = count + 1
                    temp.append((a,b+1))
            count += 1
            nextTime = temp
        for i in xrange(row):
            for j in xrange(col):
                result[i][j] = dic[(i,j)]
        return result
        

#==============================================================================
# class Solution(object):
#       #DP的思路，但是会导致死循环
#     def updateMatrix(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         row = len(matrix)
#         col = len(matrix[0])
#         self.matrix = matrix
#         self.dic = {}
#         for i in xrange(row):
#             self.dic[(i,-1)] = float('inf')
#             self.dic[(i,col)] = float('inf')
#         for i in xrange(col):
#             self.dic[(-1,i)] = float('inf')
#             self.dic[(row,i)] = float('inf')
#         result = [[0] * col for _ in xrange(row)]
#         for i in xrange(row):
#             for j in xrange(col):
#                 result[i][j] = self.helper(i,j)
#         return result
#     def helper(self,x,y):
#         if (x,y) in self.dic:
#             return self.dic[(x,y)]
#         elif self.matrix[x][y] == 0:
#             temp = 0
#         else:
#             temp = min(self.helper(x-1,y),self.helper(x+1,y),self.helper(x,y-1),self.helper(x,y+1))+1
#         self.dic[(x,y)] = temp
#         return temp
#==============================================================================
        
s = Solution()
print s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
            