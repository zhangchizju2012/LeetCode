#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:39:19 2017

@author: zhangchi
"""

# 有一个字符串它的构成是词+空格的组合，如“苹果 苹果 梨 梨”，
# 要求输入一个匹配模式（简单的以字符来写）， 比如 aabb, 来判断该字符串是否符合该模式。


class Solution(object):
    def checkPattern(self, string, pattern):
        vocabularyList = string.split(" ")
        if len(vocabularyList) != len(pattern):
    		return False
        dic = {}
        temp = set()
        for i, item in enumerate(vocabularyList):
            if item not in dic:
                if pattern[i] in temp:
                    return False
                else:
                    dic[item] = pattern[i]
                    temp.add(pattern[i])
            else:
                if dic[item] != pattern[i]:
                    return False
        return True
s = Solution()
print s.checkPattern("b b d c","aabb")