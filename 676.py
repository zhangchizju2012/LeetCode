#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 19:41:24 2017

@author: zhangchi
"""

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for item in dict:
            length = len(item)
            if length not in self.dic:
                self.dic[length] = [item]
            else:
                self.dic[length].append(item)
        
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        length = len(word)
        if length not in self.dic:
            return False
        else:
            candidateList = self.dic[length]
            for candidate in candidateList:
                for i in xrange(length):
                    if candidate[i] != word[i]:
                        if candidate[i+1:] == word[i+1:]:
                            return True
                        else:
                            break
            return False
        