#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 21:03:00 2017

@author: zhangchi
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.dic = {}
        row = len(board)
        length = len(board[0])
        for i in xrange(row):
            for j in xrange(length):
                if board[i][j] not in self.dic:
                    self.dic[board[i][j]] = [(i,j)]
                else:
                    self.dic[board[i][j]].append((i,j))
        self.length = len(word)
        if self.length == 0:
            return True
        self.word = word
        index = 0
        if word[index] not in self.dic:
            return False
        temp = self.dic[word[index]]
        for (a,b) in temp:
            if self.helper(a,b,1,{(a,b):1}):
                return True
        return False
                
        
    def helper(self,a,b,index,searched):
        if index == self.length:
            return True
        else:
            if self.word[index] in self.dic:
                if ((a-1,b) not in searched) and ((a-1,b) in self.dic[self.word[index]]):
                    search = dict(searched)
                    search[(a-1,b)] = 1
                    if self.helper(a-1,b,index+1,search):
                        return True
                if ((a+1,b) not in searched) and ((a+1,b) in self.dic[self.word[index]]):
                    search = dict(searched)
                    search[(a+1,b)] = 1
                    if self.helper(a+1,b,index+1,search):
                        return True
                if ((a,b-1) not in searched) and ((a,b-1) in self.dic[self.word[index]]):
                    search = dict(searched)
                    search[(a,b-1)] = 1
                    if self.helper(a,b-1,index+1,search):
                        return True
                if ((a,b+1) not in searched) and ((a,b+1) in self.dic[self.word[index]]):
                    search = dict(searched)
                    search[(a,b+1)] = 1
                    if self.helper(a,b+1,index+1,search):
                        return True
            return False
            
s = Solution()
board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
word = "SFDECSECB"
print s.exist(board,word)