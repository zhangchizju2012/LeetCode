#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:18:19 2017

@author: zhangchi
"""

class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = [max(item,item[::-1]) for item in strs]
        result = ""
        for i in range(len(strs)):
            for item in [strs[i],strs[i][::-1]]:
                for j in range(len(item)):
                    result = max(result,item[j:]+"".join(strs[i+1:]+strs[:i])+item[:j])
        return result

s = Solution()
print s.splitLoopedString(["abz","yab"])