#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 21:46:42 2017

@author: zhangchi
"""

class Solution(object):
    def helper(self, word):
        leftCandidate = []
        rightCandidate = []
        for i in xrange(len(word)*2+1):
            left = word[:(i//2)]
            right = word[(i+1)//2:]
            if len(left) < len(right):
                left = left[::-1]
                if left == right[:len(left)]:
                    leftCandidate.append(right[len(left):][::-1])
            elif len(left) > len(right):
                left = left[::-1]
                if right == left[:len(right)]:
                    rightCandidate.append(left[len(right):])
            else:
                if left == right[::-1]:
                    leftCandidate.append('')
                    rightCandidate.append('')
        return leftCandidate, rightCandidate
                    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic = {}
        for index,word in enumerate(words):
            dic[word] = index
        result = set()
        for word in words:
            pos = dic[word]
            left, right = self.helper(word)
            for item in left:
                if item in dic and item != word:
                    result.add((dic[item],pos))
            for item in right:
                if item in dic and item != word:
                    result.add((pos,dic[item]))
        return [list(item) for item in result]
            
s = Solution()
print s.palindromePairs(["abba",""])
