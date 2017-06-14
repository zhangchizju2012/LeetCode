#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 01:06:54 2017

@author: zhangchi
"""

class Solution(object):
    # 看看这个思路能不能用来优化69，印象中69也是用类似binary search之类的
    # 这题完全是我自己写的
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        while True:
            end = num // start
            # 差值在1以上还不能判断，如果差2的话取平均值作为start,之后得到的差值应该为1或者0，不可能还是2
            # 差值>2同理
            # 如果差1肯定就不行了
            if abs(start-end) == 1:
                return False
            if start == end:
                if num % start == 0:
                    return True
                    # 差值为0还有余数肯定不行
                else:
                    return False
            # 更新start
            start = (start + end) // 2

s = Solution()
print s.isPerfectSquare(222222222222222)