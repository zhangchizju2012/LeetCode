#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:09:23 2017

@author: zhangchi
"""

class Solution(object):
    # bfs, a little bit slow, can be solved by dfs.
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        from Queue import Queue
        q = Queue()
        d = {}
        q.put(s)
        d[s] = 1
        while q.empty() is False:
            tempS = q.get()
            if self.checkValid(tempS) == True:
                if len(result) == 0:
                    result.append(tempS)
                else:
                    if len(tempS) == len(result[0]):
                        result.append(tempS)
                    else:
                        return result
            else:
                for i in xrange(len(tempS)):
                    if tempS[i] in "()":
                        changeS = tempS[:i] + tempS[i+1:]
                        if changeS not in d:
                            d[changeS] = 1
                            q.put(changeS)
        return result # for ['']
    
    def checkValid(self, s):
        count = 0
        for item in s:
            if item == "(":
                count += 1
            elif item == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0
        
s = Solution()
print s.removeInvalidParentheses("()())()")