#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 00:34:44 2017

@author: zhangchi
"""

class Solution(object):
    # k种间隔，将间隔处理为1,2,3...k最简单，先考虑最大的，再考虑第二大的，这样可以在前k+1个
    # 数中获得，剩余的按顺序补上去就好，间隔不会在以上间隔之外
    # 最开始考虑问题，在想1，2，4，7，11再补充剩余的，发现有问题
    # 后有考虑1，2，4，3，6，5，也会有问题（如n=3,k=2）
    # 所以考虑从最大的间隔开始考虑
    # 自己想的
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        label = True
        result = [1]
        for i in xrange(k,0,-1):
            if label == True:
                result.append(result[-1]+i)
                label = False
            else:
                result.append(result[-1]-i)
                label = True
        for i in xrange(k+2,n+1):
            result.append(i)
        return result
    
s = Solution()
print s.constructArray(10,4)