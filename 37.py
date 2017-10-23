#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 21:37:45 2017

@author: zhangchi
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        full = set(["1","2","3","4","5","6","7","8","9"])
        
        left = {}
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == ".":
                    left[(i,j)] = set()
                    
        for i in xrange(9):
            temp = set()
            indexList = []
            for j in xrange(9):
                if board[i][j] != ".":
                    temp.add(board[i][j])
                else:
                    indexList.append(j)
            for j in indexList:
                left[(i,j)] = left[(i,j)].union(temp)
                    
        for i in xrange(9):
            temp = set()
            indexList = []
            for j in xrange(9):
                if board[j][i] != ".":
                    temp.add(board[j][i])
                else:
                    indexList.append(j)
            for j in indexList:
                left[(j,i)] = left[(j,i)].union(temp)
                
        for m in xrange(3):
            for n in xrange(3):
                temp = set()
                for i in xrange(3):
                    for j in xrange(3):
                        if board[3*m+i][3*n+j] != ".":
                            temp.add(board[3*m+i][3*n+j])
                for i in xrange(3):
                    for j in xrange(3):
                        if (3*m+i,3*n+j) in left:
                            left[(3*m+i,3*n+j)] = left[(3*m+i,3*n+j)].union(temp)
                            
        for i in xrange(9):
            for j in xrange(9):
                if (i,j) in left:
                    left[(i,j)] = full.difference(left[(i,j)])
                    
        return self.helper(dict(left), list(board))
        
                    
    def helper(self, lastLeft, lastBoard):
        if len(lastLeft) == 0:
            return lastBoard
        else:
            temp = [(item,lastLeft[item]) for item in lastLeft]
            temp.sort(key=lambda x:len(x[1]))
            if len(temp[0][1]) > 0:
                for value in temp[0][1]:
                    left = dict(lastLeft)
                    board = list(lastBoard)
                    
                    position = temp[0][0]
                    board[position[0]][position[1]] = value
                        
                    left.pop(position)
                    
                    for i in xrange(9):
                        if (i,position[1]) in left and value in left[(i,position[1])]:
                            left[(i,position[1])].remove(value)
                        if (position[0],i) in left and value in left[(position[0],i)]:
                            left[(position[0],i)].remove(value)
                    m = position[0] // 3
                    n = position[1] // 3
                    for i in xrange(3):
                        for j in xrange(3):
                            if (3*m+i,3*n+j) in left and value in left[(3*m+i,3*n+j)]:
                                left[(3*m+i,3*n+j)].remove(value)
                            
                    
                    result = self.helper(dict(left), list(board))
                    if result is not None:
                        return result
                        
                        
    
s = Solution()
a = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
# =============================================================================
# a = [["5","3",".",".","7",".",".",".","."],
#      ["6",".",".","1","9","5",".",".","."],
#      [".","9","8",".",".",".",".","6","."],
#      ["8",".",".",".","6",".",".",".","3"],
#      ["4",".",".","8",".","3",".",".","1"],
#      ["7",".",".",".","2",".",".",".","6"],
#      [".","6",".",".",".",".","2","8","."],
#      [".",".",".","4","1","9",".",".","5"],
#      [".",".",".",".","8",".",".","7","9"]]
# =============================================================================
print s.solveSudoku(a)