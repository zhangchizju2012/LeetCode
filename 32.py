#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Reviewed on Sat Oct 21 12:24:03 2017

@author: zhangchi
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for index, item in enumerate(s):
            if item == "(":
                stack.append(index)
            else:
                if len(stack) > 0 and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(index)
        stack = [-1] + stack + [len(s)]
        result = 0
        for i in xrange(len(stack)-1):
            result = max(result, stack[i+1]-stack[i]-1)
        return result
                    

# =============================================================================
# class Solution(object):
#     # 错的，没考虑这种 "(()(((()"
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         result = 0
#         count = 0
#         temp = 0
#         stack = []
#         for item in s:
#             if item == "(":
#                 temp += 1
#             else:
#                 if temp > 0:
#                     temp -= 1
#                     count += 1
#                     if temp == 0:
#                         stack.append(count)
#                         count = 0
#                 else:
#                     result = max(result, sum(stack))
#                     stack = []
#                     temp = 0
#                     count = 0
#         result = max(result, count, sum(stack))
#         return result * 2
# =============================================================================



# =============================================================================
# """
# Created on Fri Jun 23 12:05:11 2017
# 
# @author: zhangchi
# """
# 
# 
# class Solution(object):
#     # 看了答案：https://discuss.leetcode.com/topic/2289/my-o-n-solution-using-a-stack
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         stack = [-1] # 为了配合得到最后的结果
#         for index,item in enumerate(s):
#             if item == "(":
#                 stack.append(index)
#             else:
#                 if len(stack) > 1 and s[stack[-1]] == "(": # > 1是配合stack=[-1]
#                     stack.pop()
#                 else: # 处理()))))这种情况，len(stack)==1是添加第二个）,s[stack[-1]] != "("是添加后续的）
#                     stack.append(index)
#         stack.append(len(s))
#         result = -float('inf')
#         for i in xrange(len(stack)-1):
#             result = max(result,stack[i+1]-stack[i]-1)
#         return result
#         
# =============================================================================
s = Solution()
#print s.longestValidParentheses(")()(((())))(")
print s.longestValidParentheses("()(()")
#print s.longestValidParentheses("(()(((()")