#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 21:15:49 2017

@author: zhangchi
"""

# 0914.2017复习，
# 另一种想法，从左到右，从短到常考虑
# 可以从左到右扫描，先考虑一个字符，一个字符直接就是回文了，然后增加一个，然后两个分开肯定是回文，然后再往前扫描
# 还可能存在回文的。
# 当前面存在n个了的时候，再加一个，然后这一个加上前m（需要循环过去），可能还是回文，然后和前m之前的（通过dic查询），进行合并
# 这一小部分有点像我uncertain graph link prediction的算法
# dic里储存，长度为m时的结果


class Solution(object):
    # DP, use for loop instead of recursion
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        dic = {}
        length = len(s)
        for i in xrange(length+1):
            dic[i] = []
        dic[length].append([])
        # line22: for the case such as "ccaba", it will result in error in line 29 if no this line
        dic[length-1].append([s[-1]]) 
        for i in xrange(length-2,-1,-1):
            for j in xrange(i,length):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    for item in dic[j+1]:
                        dic[i].append([temp]+item)
        return dic[0]
                
s = Solution()
a = "aab"
print s.partition(a)
        