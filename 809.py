#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 19:38:41 2018

@author: zhangchi
"""

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if len(S) == 0:
            count = 0
            for item in words:
                if item == S:
                    count += 1
            return count
        else:
            self.ground = []
            last = S[0]
            count = 1
            for i in range(1,len(S)):
                if S[i] == last:
                    count += 1
                else:
                    self.ground.append([last,count])
                    last = S[i]
                    count = 1
            self.ground.append([last,count])
            #print(self.ground)
            result = 0
            for item in words:
                if self.helper(item) is True:
                    #print(item)
                    result += 1
            return result
            
    def helper(self, S):
        if len(S) == 0:
            return False
        else:
            temp = []
            last = S[0]
            count = 1
            for i in range(1,len(S)):
                if S[i] == last:
                    count += 1
                else:
                    temp.append([last,count])
                    last = S[i]
                    count = 1
            temp.append([last,count])
            #print(temp)
            if len(temp) != len(self.ground):
                return False
            else:
                for a,b in zip(temp, self.ground):
                    if a[0] == b[0] and (b[1]>=3 or b[1] == a[1]):#(b[1] - a[1] >= 2 or b[1] - a[1] == 0):
                        pass
                    else:
                        return False
                return True
            
s = Solution()
#print s.expressiveWords("heeellooo",["hello", "hi", "helo"])
#"dddiiiinnssssssoooo",["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]
print s.expressiveWords("dddiiiinnssssssoooo",["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"])