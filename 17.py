#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:18:47 2016

@author: zhangchi
"""
#递归
class Solution(object):
    def __init__(self):
        self.dictionary = {'1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
    def letterCombinations(self, digits):
        length = len(digits)
        if length == 0:
            return []
        elif length == 1:
            string = self.dictionary[digits]
            return [string[i] for i in range(len(string))]
        else:
            result = []
            for item in self.letterCombinations(digits[:length-1]):
                temp = self.dictionary[digits[length-1]]
                for i in range(len(temp)):
                    result.append(item+temp[i])
            return result
                    
S = Solution()
print S.letterCombinations('23')
    