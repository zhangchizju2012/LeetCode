#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 19:48:06 2018

@author: zhangchi
"""

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        dic = {}
        for index, item in enumerate(S):
            if item in dic:
                dic[item].append(index)
            else:
                dic[item] = [index]
                
        count = 0
        for item in words:
            index = -1
            item_label = True
            for ch in item:
                if ch not in dic:
                    item_label = False 
                    break
                else:
                    label = False
                    index_list = dic[ch]
                    for token in index_list:
                        # 要用就用第一个，给后面的index留足空间
                        if token > index:
                            index = token
                            label = True
                            break
                    if label is False:
                        item_label = False 
                        break
            if item_label is True:
                count += 1
            
        return count
    
s = Solution()
print(s.numMatchingSubseq("abcde",["a", "bb", "acd", "ace"]))