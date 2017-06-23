#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 12:05:11 2017

@author: zhangchi
"""

class Solution(object):
    # 看了答案：https://discuss.leetcode.com/topic/2289/my-o-n-solution-using-a-stack
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1] # 为了配合得到最后的结果
        for index,item in enumerate(s):
            if item == "(":
                stack.append(index)
            else:
                if len(stack) > 1 and s[stack[-1]] == "(": # > 1是配合stack=[-1]
                    stack.pop()
                else: # 处理()))))这种情况，len(stack)==1是添加第二个）,s[stack[-1]] != "("是添加后续的）
                    stack.append(index)
        stack.append(len(s))
        result = -float('inf')
        for i in xrange(len(stack)-1):
            result = max(result,stack[i+1]-stack[i]-1)
        return result
        
s = Solution()
print s.longestValidParentheses("")