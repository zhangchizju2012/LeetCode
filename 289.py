#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:51:07 2017

@author: zhangchi
"""

class Solution(object):
    # 还有更好的解法：https://discuss.leetcode.com/topic/29054/easiest-java-solution-with-explanation
    # 没有用额外的空间，利用bit来储存之前和之后的信息
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dic = {}
        row = len(board)
        length = len(board[0])
        for i in xrange(-1,length+1):
            self.dic[(-1,i)] = 0
            self.dic[(row,i)] = 0
        for i in xrange(-1,row+1):
            self.dic[(i,-1)] = 0
            self.dic[(i,length)] = 0
        for i in xrange(row):
            for j in xrange(length):
                self.dic[(i,j)] = board[i][j]
        for i in xrange(row):
            for j in xrange(length):
                count = self.helper(i,j)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                else:
                    if count == 3:
                        board[i][j] = 1
                    
        
    def helper(self, i, j):
        count = 0
        if self.dic[(i-1,j-1)] == 1:
            count += 1
        if self.dic[(i-1,j)] == 1:
            count += 1
        if self.dic[(i-1,j+1)] == 1:
            count += 1
        if self.dic[(i,j-1)] == 1:
            count += 1
        if self.dic[(i,j+1)] == 1:
            count += 1
        if self.dic[(i+1,j-1)] == 1:
            count += 1
        if self.dic[(i+1,j)] == 1:
            count += 1
        if self.dic[(i+1,j+1)] == 1:
            count += 1
        return count
        
s = Solution()
print s.gameOfLife([[0,0]])
            