#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 20:04:45 2017

@author: zhangchi
"""

class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        dic = {0:1,1:2,2:3}
        for i in range(3,32):
            dic[i] = dic[i-2] + dic[i-1]
        # n位数，满足条件的有多少可能，如n=3,满足条件的有000,100,010,001,101，
        temp = [0] * 32
        for i in range(32):
            if num & (2**i) > 0:
                temp[i] = 1
        temp = temp[::-1]
        # 把num用二进制表示出来
        result = 0
        for index, item in enumerate(temp):
            if item == 1:
                if index == 0 or temp[index-1] == 0:
                # 当第n位为1且其前一位不是1，那就令n位及更高位都为0，然后剩下的就是n-1位，剩下的n-1位任取值，肯定小于num
                # 在考虑时候位的时候，要将n位视为1，所以有后面的else情况 
                    result += dic[31-index]
                else:
                # 当连续出现两个1的时候，就可以终止了(用1101，101，110，1110（都是二进制）这几个例子试试)
                    result += dic[31-index]
                    return result
        result += 1
        # 如果到了最后，说明他本身也是满足条件的
        return result
        
s = Solution()
print s.findIntegers(4)