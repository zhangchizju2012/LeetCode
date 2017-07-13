#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 00:55:42 2017

@author: zhangchi
"""

class Solution(object):
    # 自己写的
    # one-pass, using only O(1) extra memory and without modifying
    # 2d matrix
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = len(board)
        length = len(board[0])
        count = 0
        for i in xrange(row):
            previous = '.' # 用来确定横排的情况
            for j in xrange(length):
                if board[i][j] == 'X':
                    if previous == '.' and (i==0 or board[i-1][j] == '.'): # and后面用来确定纵排的情况
                        count += 1
                    previous = 'X'
                else:
                    previous = '.'
        return count
                    