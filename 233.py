#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:53:43 2017

@author: zhangchi
"""

class Solution(object):
    # 自己做的
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = len(str(n+1)) # +1是因为还要包含自己本身，而后面的处理是按不包含自己本身处理的
        self.dic = {0:0,1:1}
        # 这里的值分别表示，n个9时，结果为多少，如，99时，答案为20，999时，答案为300 ...
        for i in xrange(2,length):
            self.dic[i] = self.dic[i-1] * 10 + 10 ** (i - 1)
        return self.helper(n+1) # +1是因为还要包含自己本身，而后面的处理是按不包含自己本身处理的
        
    def helper(self, n):
        if n == 0:
            return 0
        length = len(str(n))
        count = n // (10 ** (length-1))
        result = 0
        for i in xrange(count):
            result += self.dic[length-1]
            if i == 1: # 1打头时要特殊处理
                result += 10 ** (length - 1)
        temp = n % (10 ** (length-1))
        if count == 1: # 1打头时要特殊处理
            result += temp
        result += self.helper(temp) # recursion
        return result
        
s = Solution()
print s.countDigitOne(99999)