#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:57:54 2017

@author: zhangchi
"""

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for i in xrange(max(0,num-6),min(4,num)+1):
            left = self.helper(4,i)
            right = self.helper(6,num-i)
            for itemLeft in left:
                for itemRight in right:
                    rightStr = str(itemRight)
                    if len(rightStr) == 1:
                        rightStr = "0" + rightStr
                    result.append(str(itemLeft)+":"+rightStr)
        return result
        
    def helper(self,number,count):
        if count == 0:
            return [0]
        if number == 4:
            temp = [1,2,4,8]
            up = 12
        else:
            temp = [1,2,4,8,16,32]
            up = 60
        dic = {}
        change = {}
        for value in temp:
            for item in dic:
                if dic[item] < count:
                    change[item + value] = dic[item] + 1
            change[value] = 1
            dic = dict(change)
        result = []
        for item in dic:
            if dic[item] == count and item < up:
                result.append(item)
        return result
        
s = Solution()
print s.readBinaryWatch(1)