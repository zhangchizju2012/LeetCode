#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:30:22 2017

@author: zhangchi
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for item in s:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        back = {}
        freq = []
        for item in dic:
            if dic[item] in back:
                back[dic[item]].append(item)
            else:
                back[dic[item]] = [item]
                freq.append(dic[item])
        freq.sort(reverse=True)
        result = ""
        for i in freq:
            for item in back[i]:
                result += item * i
        return result
        
s = Solution()
print s.frequencySort("Aabbccddcddeeee")
        