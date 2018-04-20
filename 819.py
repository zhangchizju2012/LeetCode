#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:53:50 2018

@author: zhangchi
"""

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set()
        for item in banned:
            ban.add(item)
        dic = {}
        temp = "!?',;."
        stop = set()
        for item in temp:
            stop.add(item)
        paragraph = paragraph.split()
        for item in paragraph:
            item = item.lower()
            if item[-1] in stop:
                item = item[:-1]
            if item not in ban:
                if item not in dic:
                    dic[item] = 1
                else:
                    dic[item] += 1
        result = ""
        count = -float('inf')
        for item in dic:
            if dic[item] > count:
                count = dic[item]
                result = item
        return result
    
s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))