#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:16:27 2017

@author: zhangchi
"""

class Solution(object):
    # 两次提交错误的情况我都预料到了的，实在是太无聊了，不要管
    # 思路： 从四周向中间延伸，碰到X只能停止，碰到O都可以继续延伸
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        temp = {}
        row = len(board)
        if row > 0:
            lenght= len(board[0])
            # 方便查询，并且延伸一层，避免之后大量的if else
            for i in xrange(row):
                for j in xrange(lenght):
                    temp[(i,j)] = board[i][j]
            # 延伸一层并置为X，避免之后大量的if else
            for i in xrange(-1,row+1):
                temp[(i,-1)] = "X"
                temp[(i,lenght)] = "X"
            for i in xrange(lenght):
                temp[(-1,i)] = "X"
                temp[(row,i)] = "X"
    
            stack = []
            dic = {}
            # 最外层符合条件的先进行添加
            for i in xrange(row):
                if temp[(i,0)] == "O":
                    stack.append((i,0))
                    dic[(i,0)] = 1
                if temp[(i,lenght-1)] == "O":
                    stack.append((i,lenght-1))
                    dic[(i,lenght-1)] = 1
                        
            for i in xrange(1,lenght-1):
                if temp[(0,i)] == "O":
                    stack.append((0,i))
                    dic[(0,i)] = 1
                if temp[(row-1,i)] == "O":
                    stack.append((row-1,i))
                    dic[(row-1,i)] = 1
            # 逐渐往里探索，这里用stack的pop,append其实没有什么实际的意义，用queue之类的都是一样的，只是想一个一个找过去
            while len(stack) > 0:
                (a,b) = stack.pop()
                # not in dic是为了避免重复查询
                if temp[(a-1,b)] == "O" and (a-1,b) not in dic:
                    dic[(a-1,b)] = 1
                    stack.append((a-1,b))
                if temp[(a+1,b)] == "O" and (a+1,b) not in dic:
                    dic[(a+1,b)] = 1
                    stack.append((a+1,b))
                if temp[(a,b-1)] == "O" and (a,b-1) not in dic:
                    dic[(a,b-1)] = 1
                    stack.append((a,b-1))
                if temp[(a,b+1)] == "O" and (a,b+1) not in dic:
                    dic[(a,b+1)] = 1
                    stack.append((a,b+1))
                    
            result = [["O"]*lenght for _ in xrange(row)]
            for i in xrange(row):
                for j in xrange(lenght):
                    if (i,j) not in dic:
                        result[i][j] = "X"
                        
            for i in xrange(row):
                board[i] = "".join(result[i])
            return board
                    
s = Solution()
print s.solve(["XXXX","XOOX","XXOX","XOXX"])

                