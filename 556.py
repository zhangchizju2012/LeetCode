#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:16:08 2017

@author: zhangchi
"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = []
        while n != 0:
            temp.append(n%10)
            n = n // 10
        
        label = False
        label2 = False
        for i in range(len(temp)-1):
            for j in range(i+1,len(temp)):
                if temp[i] < temp[j]:
                    label2 = True
                elif temp[i] == temp[j] and label2 == True:
                    label2 = False
                    break
                elif temp[i] > temp[j]:
                    t = temp[i]
                    temp[:j] = sorted(temp[:i]+temp[i+1:j+1],reverse=True)
                    temp[j] = t
                    label = True
                    break
            if label == True:
                break
        if label == False:
            return -1
        result = 0
        count = 0
        for item in temp:
            result += item * (10 ** count)
            count += 1
        if result >= 2147483648:
            return -1
        return result

s = Solution()
#print s.nextGreaterElement(12443322)
print s.nextGreaterElement(1999999999)
#print s.nextGreaterElement(1237654)