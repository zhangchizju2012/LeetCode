#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 01:55:21 2017

@author: zhangchi
"""

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        self.k = k
        self.result = []
        if len(s) == 0:
            return 0
        self.helper(s)
        if len(self.result) == 0:
            return 0
        else:
            return max(self.result)

    def helper(self, s):
        dic = {}
        for item in s:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        stop = {}
        for item in dic:
            if dic[item] < self.k:
                stop[item] = 1
        # stop是没有符合要求的字母序列, 符合k要求的string肯定不能包含stop词
        if len(stop) == 0:
            self.result.append(len(s))
        else:
            temp = []
            start = end = 0
            for i in xrange(len(s)):
                if s[i] not in stop:
                    end += 1
                else:
                    if end - start > 0:
                        temp.append(s[start:end])
                    start = end = i + 1
            if end - start > 0:
                temp.append(s[start:end])
            # 按照stop词切割出新的string, 然后递归调用这个函数，知道切出的string完全符合k的要求，即line 38, line 39
            for item in temp:
                self.helper(item)
                
s = Solution()
print s.longestSubstring("bbaaacbd",3)