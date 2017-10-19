#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 16:48:40 2017

@author: zhangchi
"""

class Solution(object):
    # 复习，完全自己写的
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        stack = 0
        count = 0
        leftCount = 0
        rightCount = 0
        # 统计有效的对数，以及（和）的总数
        for item in s:
            if item == "(":
                stack += 1
                count += 1
                leftCount += 1
            elif item == ")":
                rightCount += 1
                if stack > 0:
                    stack -= 1
                    count += 1
                else:
                    pass
        self.number = (count - stack) // 2 # 应该留下的总对数
        self.length = len(s) 
        self.leftCanThrow = leftCount - self.number # 应该丢弃的左括号的总数
        self.rightCanThrow = rightCount - self.number # 应该丢弃的右括号的总数
        self.result = set()
        self.s = s
        self.helper("",0,0,0,0,0)
        return list(self.result)
        
        
    def helper(self,now,leftUsed,leftThrow,rightUsed,rightThrow,index):
        # leftUsed: 已经留下的左括号的数量
        # leftThrow: 已经丢弃的左括号的数量
        # 思路: 只想每个字符，都存在可以保留，可以丢弃的选项
        if index == self.length:
            self.result.add(now)
        else:
            item = self.s[index]
            if item == "(":
                if leftUsed < self.number:
                    self.helper(now+"(",leftUsed+1,leftThrow,rightUsed,rightThrow,index+1)
                if leftThrow < self.leftCanThrow:
                    self.helper(now,leftUsed,leftThrow+1,rightUsed,rightThrow,index+1)
            elif item == ")":
                if rightUsed < leftUsed and rightUsed < self.number:
                    self.helper(now+")",leftUsed,leftThrow,rightUsed+1,rightThrow,index+1)
                if rightThrow < self.rightCanThrow:
                    self.helper(now,leftUsed,leftThrow,rightUsed,rightThrow+1,index+1)
            else:
                self.helper(now+item,leftUsed,leftThrow,rightUsed,rightThrow,index+1)
                
s = Solution()
print s.removeInvalidParentheses("(a)())()")
        