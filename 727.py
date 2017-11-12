#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 20:16:56 2017

@author: zhangchi
"""

class Solution(object):
    # 开始想着dp，后来觉着不用，稍微更新一下就好了，见line35
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic = {}
        for index, item in enumerate(S):
            if item not in dic:
                dic[item] = [index]
            else:
                dic[item].append(index)
                
        for item in T:
            if item not in dic:
                return ""
        candidate = [[item,item] for item in dic[T[0]]]
        
        for i in xrange(1,len(T)):
            key = T[i]
            temp = dic[key]
            pointCandidate = 0
            pointTemp = 0
            # 核心在这里
            # candidate的每个元素是满足条件的index的起始和终止，然后我们把T中的元素一个一个拿来考虑
            while pointCandidate < len(candidate) and pointTemp < len(temp):
                if candidate[pointCandidate][1] >= temp[pointTemp]:
                    pointTemp += 1
                else:
                    candidate[pointCandidate][1] = temp[pointTemp]
                    pointCandidate += 1
            # 这部分的要抛弃掉
            if pointCandidate < len(candidate):
                candidate = candidate[:pointCandidate]
                
        length = float('inf')
        result = ""
        for i,j in candidate:
            if j-i < length:
                length = j-i
                result = S[i:j+1]
        return result
    
    
s = Solution()
# =============================================================================
# a="cnhczmccqouqadqtmjjzl"
# b="mq"
# =============================================================================
a = "cnhczmccqouqadqtmjjzl"
b = "mm"
#print s.minWindow("abcdebdde", "bde")
print s.minWindow(a,b)