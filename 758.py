#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:40:06 2018

@author: zhangchi
"""

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        positionList = []
        for item in words:
            last = -1
            while True:
                last = S.find(item, last + 1)
                if last == -1:
                    break
                else:
                    positionList.append([last,last+len(item)])
        positionList.sort(key=lambda x:x[1])
        positionList.sort(key=lambda x:x[0])
        #print positionList
        
        result = []
        for item in positionList:
            if len(result) == 0:
                result.append(item)
            else:
                if result[-1][0] <= item[0] <= result[-1][1]:
                    result[-1][1] = max(result[-1][1], item[1])
                else:
                    result.append(item)
                    
        if len(result) == 0:
            return S
        else:
            output = S[:result[0][0]]
            for index in xrange(len(result)):
                output += "<b>" + S[result[index][0]:result[index][1]] + "</b>"
                if index < len(result) - 1:
                    output += S[result[index][1]:result[index+1][0]]
            output += S[result[-1][1]:]
            return output
    
s = Solution()
print s.boldWords(["ab", "bc"] ,"aabcabc")
print s.boldWords(["ab", "bc"],"aabcd")
print s.boldWords([],"")
print s.boldWords(["ccb","b","d","cba","dc"],"eeaadadadc")