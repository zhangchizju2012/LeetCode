#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:24:42 2017

@author: zhangchi
"""

class Solution(object):
    # 按照实际运行过程写一下代码就可以了
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.dic = {n:1}
        temp = n
        while True:
            temp = self.helper(temp)
            if temp == 1:
                return True
            elif temp in self.dic:
                return False
            self.dic[temp] = 1
                
    def helper(self, n):
        result = 0
        while n != 0:
            temp = n % 10
            result += temp ** 2
            n = n // 10
        return result
        
s = Solution()
print s.isHappy(19)