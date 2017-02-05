#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:45:54 2016

@author: zhangchi
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #先放好棋盘，再判断是否有效，更高效的做法是边摆棋盘边判断是否有效
        for item in board:
            if self.checkValid(item) == False:
                return False
        
        newBoard = [""]*9
        for item in board:
            for i in range(9):
                newBoard[i] = newBoard[i] + item[i]
        for item in newBoard:
            if self.checkValid(item) == False:
                return False
                
        groupBoard = [""]*9
        #此处可以精简 #leetcode这里会报错，不知为什么
        for item in board[0:3]:
            for i in range(3):
                groupBoard[i] = groupBoard[i] + item[i*3:i*3+3]
        for item in board[3:6]:
            for i in range(3):
                groupBoard[i+3] = groupBoard[i+3] + item[i*3:i*3+3]
        for item in board[6:9]:
            for i in range(3):
                groupBoard[i+6] = groupBoard[i+6] + item[i*3:i*3+3]
        for item in groupBoard:
            if self.checkValid(item) == False:
                return False
        return True
        
    def checkValid(self,nineNumbers):
        sortedNumbers = sorted(nineNumbers)
        length = len(sortedNumbers)
        for item in range(length):
            if item > 0 and sortedNumbers[item] != '.' and sortedNumbers[item] == sortedNumbers[item-1]:
                return False
        return True

S = Solution()
board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print S.isValidSudoku(board)