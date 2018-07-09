#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 20:11:55 2018

@author: zhangchi
"""

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 2
        elif N <= 7:
            for i in range(N, 8):
                if self.testPrime(i):
                    return i
        elif N < 10:
            return 11
        else:
            s = str(N)
            length = len(s)
            if length % 2 == 0:
                temp = s[:length//2]
                if int(temp+temp[::-1]) >= N and self.testPrime(int(temp+temp[::-1])):
                    return int(temp+temp[::-1])
                for i in range(int(temp)+1, int(length//2*'9')+1):
                    left = str(i)
                    if self.testPrime(int(left+left[::-1])):
                        return int(left+left[::-1])
                return self.primePalindrome(int('1'+length*'0'))
            else:
                left = s[:length//2+1]
                if int(left+left[:-1][::-1]) >= N and self.testPrime(int(left+left[:-1][::-1])):
                    return int(left+left[:-1][::-1])
                for i in range(int(s[:length//2+1])+1, int((length//2+1)*'9')+1):
                    left = str(i)
                    if self.testPrime(int(left+left[:-1][::-1])):
                        return int(left+left[:-1][::-1])
                return self.primePalindrome(int('1'+length*'0'))
                    
        
    def testPrime(self, value):
        for i in range(2, int(value ** 0.5) + 1):
            if value % i == 0:
                return False
        return True
    
s = Solution()
print s.primePalindrome(43265473)