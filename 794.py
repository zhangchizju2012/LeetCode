#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 19:33:14 2018

@author: zhangchi
"""

class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        self.board = board
        o_count = 0
        x_count = 0
        for line in board:
            for item in line:
                if item == "O":
                    o_count += 1
                elif item == "X":
                    x_count += 1
                    
        if o_count > x_count or (x_count - o_count) > 1:
            return False
        
        o_win = self.helper("O")
        x_win = self.helper("X")
        if o_win + x_win > 1:
            return False
        
        if x_win == 1:
            if x_count - o_count != 1:
                return False
            
        if o_win == 1:
            if x_count - o_count != 0:
                return False
        
        return True
        
    def helper(self, ch):
        count = 0
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == ch:
            count += 1
        if self.board[1][0] == self.board[1][1] == self.board[1][2] == ch:
            count += 1
        if self.board[2][0] == self.board[2][1] == self.board[2][2] == ch:
            count += 1
        if self.board[0][0] == self.board[1][0] == self.board[2][0] == ch:
            count += 1
        if self.board[0][1] == self.board[1][1] == self.board[2][1] == ch:
            count += 1
        if self.board[0][2] == self.board[1][2] == self.board[2][2] == ch:
            count += 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == ch:
            count += 1
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == ch:
            count += 1
        return count
    
s = Solution()
print(s.validTicTacToe(["XXX","XOO","OO "]))