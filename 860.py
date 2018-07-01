#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 18:31:28 2018

@author: zhangchi
"""

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dic = {}
        dic[5] = 0
        dic[10] = 0
        dic[20] = 0
        for item in bills:
            if item == 5:
                dic[5] += 1
            elif item == 10:
                if dic[5] == 0:
                    return False
                else:
                    dic[10] += 1
                    dic[5] -= 1
            else:
                if dic[5] == 0:
                    return False
                else:
                    if dic[10] > 0:
                        dic[20] += 1
                        dic[10] -= 1
                        dic[5] -= 1
                    else:
                        if dic[5] < 3:
                            return False
                        else:
                            dic[20] += 1
                            dic[5] -= 3
        return True
    
s = Solution()
print s.lemonadeChange([5,5,10,10,20])