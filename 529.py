#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 09:01:25 2017

@author: zhangchi
"""

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        else:
            self.helper(board, click)
        return board
            
    def helper(self, board, click):
        number = self.checkNumber(board, click)
        if number > 0:
            board[click[0]][click[1]] = str(number)
        else:
            board[click[0]][click[1]] = 'B'
            row = len(board)
            col = len(board[0])
            first = click[0]
            second = click[1]
            if first - 1 >= 0:
                if second - 1 >= 0:
                    if board[first-1][second-1] == 'E':
                        self.helper(board, [first-1,second-1])
                if board[first-1][second] == 'E':
                    self.helper(board, [first-1,second])
                if second + 1 <= col - 1:
                    if board[first-1][second+1] == 'E':
                        self.helper(board, [first-1,second+1])
                        
            if second - 1 >= 0:
                if board[first][second-1] == 'E':
                    self.helper(board, [first,second-1])
            if second + 1 <= col - 1:
                if board[first][second+1] == 'E':
                    self.helper(board, [first,second+1])
                    
            if first + 1 <= row - 1:
                if second - 1 >= 0:
                    if board[first+1][second-1] == 'E':
                        self.helper(board, [first+1,second-1])
                if board[first+1][second] == 'E':
                    self.helper(board, [first+1,second])
                if second + 1 <= col - 1:
                    if board[first+1][second+1] == 'E':
                        self.helper(board, [first+1,second+1])
    
    def checkNumber(self, board, click):
        row = len(board)
        col = len(board[0])
        first = click[0]
        second = click[1]
        count = 0
        if first - 1 >= 0:
            if second - 1 >= 0:
                if board[first-1][second-1] == 'M':
                    count += 1
            if board[first-1][second] == 'M':
                count += 1
            if second + 1 <= col - 1:
                if board[first-1][second+1] == 'M':
                    count += 1
                    
        if second - 1 >= 0:
            if board[first][second-1] == 'M':
                count += 1
        if second + 1 <= col - 1:
            if board[first][second+1] == 'M':
                count += 1
                
        if first + 1 <= row - 1:
            if second - 1 >= 0:
                if board[first+1][second-1] == 'M':
                    count += 1
            if board[first+1][second] == 'M':
                count += 1
            if second + 1 <= col - 1:
                if board[first+1][second+1] == 'M':
                    count += 1
        return count
        
s = Solution()
board = [['E', 'E', 'E', 'E', 'E'],['E', 'E', 'M', 'E', 'E'],['E', 'E', 'E', 'E', 'E'],['E', 'E', 'E', 'E', 'E']]
#board = [['E', 'E', 'E', 'E', 'E']]
click = [3,0]
print s.updateBoard(board,click)
            