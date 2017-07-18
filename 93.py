#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:57:40 2017

@author: zhangchi
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = self.helper(s,4)
        final = []
        for item in result:
            final.append(".".join([str(i) for i in item]))
        return final
    
    def helper(self, s, n):
        length = len(s)
        if length > n * 3 or length < n * 1:
            return []
        else:
            if n == 1:
                if s[0] == "0" and length > 1:
                    return []
                if int(s) < 256:
                    return [[int(s)]]
                else:
                    return []
            else:
                result = []
                for i in range(1,min(3,length)+1):
                    if int(s[:i]) < 256:
                        this = [int(s[:i])]
                        after = self.helper(s[i:],n-1)
                        if after == None:
                            print s, s[i:], n-1
                        for item in after:
                            result.append(this+item)
                        if int(s[:i]) == 0:
                            break
                return result
                
s = Solution()
print s.restoreIpAddresses("172162541")
                