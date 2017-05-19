#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:52:23 2017

@author: zhangchi
"""

class Solution(object):
    # finish by myself, before the flight, in the hotel and airport
    # 详细的说明在下方， 下面的答案只是没有考虑正方向反方向而已
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        if col == 0:
            return []
        result = []
        label = True
        # 解决对角线及以上部分
        for i in xrange(row):
            temp = []
            for j in xrange(min(i+1,col)):
                temp.append(matrix[i-j][j])
            if label == True:
                result += temp
                label = False
            else:
                result += temp[::-1]
                label = True
        # 解决对角线以下部分   
        for i in xrange(row,row+col-1):
            temp = []
            for j in xrange(row-1,max(-1,i-col),-1):
                temp.append(matrix[j][i-j])
            if label == True:
                result += temp
                label = False
            else:
                result += temp[::-1]
                label = True
        return result

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = len(matrix[0])
        result = []
        # 解决对角线及以上部分
        for i in xrange(row):
            temp = []
            for j in xrange(min(i+1,col)):
                temp.append(matrix[i-j][j])
            result += temp
        # 解决对角线以下部分   
        for i in xrange(row,row+col-1):
            temp = []
            for j in xrange(row-1,max(-1,i-col),-1):
                # 画图可以搞清楚为什么是i-col
                # row - 1 - (row + col - 2 - i) - 1 = i - row
                # 最右下角的横坐标加纵坐标是 row + col - 2，从左下到右上的起始点的横坐标和纵坐标的和为 i，
                # 两者之差即两点的（横坐标）差距（两者的纵坐标是相同的）
                # 目的是求从左下到右上的终点的纵坐标
                # 右下角的纵坐标为 row - 1, 右上角和右下的纵坐标差距应该和左下角和右下角的横坐标差距相同，所以row - 1 - (row + col - 2 - i)
                # 最后的 - 1是为了配合range
                # min是因为纵坐标最小不能小于0
                temp.append(matrix[j][i-j])
            result += temp
        return result
        
s = Solution()
#print s.findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ],[ 10, 11, 12 ]])
#print s.findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ]])
print s.findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])