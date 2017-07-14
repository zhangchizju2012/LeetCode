#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 14:52:27 2017

@author: zhangchi
"""

class Solution(object):
    # 看了答案，非常elegent的解法，temp储存扫描到第i个字符前的结果，在到第i个的时候
    # 只需要检查temp+2和temp+1长度的序列是否是回文的，少了没有意义，多了不可能是回文
    # 如果多了是回文的话，扫描到第i个字符前的结果就不止是temp了
    # 答案：https://discuss.leetcode.com/topic/21848/ac-relatively-short-and-very-clear-java-solution
    # 就看了思路，code没看也懒得看，自己写的
#==============================================================================
#     Example: "xxxbcbxxxxxa", (x is random character, not all x are equal) now we 
#           are dealing with the last character 'a'. The current longest palindrome
#           is "bcb" with length 3.
# 1. check "xxxxa" so if it is palindrome we could get a new palindrome of length 5.
# 2. check "xxxa" so if it is palindrome we could get a new palindrome of length 4.
# 3. do NOT check "xxa" or any shorter string since the length of the new string is 
#    no bigger than current longest length.
# 4. do NOT check "xxxxxa" or any longer string because if "xxxxxa" is palindrome 
#    then "xxxx" got  from cutting off the head and tail is also palindrom. It has 
#    length > 3 which is impossible.'
#==============================================================================
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = 0
        length = len(s)
        result = ""
        for index in xrange(length):
            if index-temp-1>=0 and s[index-temp-1:index+1] == s[index-temp-1:index+1][::-1]:
                result = s[index-temp-1:index+1]
                temp += 2
            elif s[index-temp:index+1] == s[index-temp:index+1][::-1]:
                result = s[index-temp:index+1]
                temp += 1
        return result
            
s = Solution()
print s.longestPalindrome("abcba")