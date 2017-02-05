#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:59:49 2016

@author: zhangchi
"""

class Solution(object):
    def helpNum(self,n,result):
        count = 0
        for i in range(n):
            if i in result:
                temp1 = result[i]
            else:
                temp1,result = self.helpNum(i,result)
                result[i] = temp1
            if n-1-i in result:
                temp2 = result[n-1-i]
            else:
                temp2,result = self.helpNum(n-1-i,result)
                result[n-1-i] = temp2
            count = count + temp1 * temp2
        return count,result
            
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = {0:1,1:1}
        count,_ = self.helpNum(n,result)
        return count

S = Solution()
print S.numTrees(5)