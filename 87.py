#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:00:26 2017

@author: zhangchi
"""
class Solution(object):
    # 可以在任意位置切断，题意有歧义
    # 有点brute force的感觉，自己做的
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        return self.helper(s1,s2)
    
    def helper(self, s1, s2):
        if len(s1) == 0 or s1 == s2:
            return True
        length = len(s1)
        for index in xrange(1,length):
            # 可以在任意位置切断
            # 有两种可能，前n个和后n个
            s1left = self.generateDic(s1[:index])
            s1right = self.generateDic(s1[index:])
            
            s2left1 = self.generateDic(s2[:index])
            s2right1 = self.generateDic(s2[index:])
            
            s2left2 = self.generateDic(s2[(-index):])
            s2right2 = self.generateDic(s2[:(-index)])
            
            if s1left == s2left1 and s1right == s2right1:
                if self.helper(s1[:index],s2[:index]) and self.helper(s1[index:],s2[index:]):
                    return True
            if s1left == s2left2 and s1right == s2right2:
                if self.helper(s1[:index],s2[(-index):]) and self.helper(s1[index:],s2[:(-index)]):
                    return True
        return False
        
    def generateDic(self, s1):
        dic = {}
        for item in s1:
            if item in dic:
                dic[item] += 1 
            else:
                dic[item] = 1
        return dic

s1 = "great"
s2 = "taegr"
#s1 = "ab"
#s2 = "ba"
s = Solution()
print s.isScramble("abb","bab")
#print s.isScramble(s1,s2)

# 以为只能在中间切断，题意有歧义，这里也提到了这个问题：https://discuss.leetcode.com/topic/861/can-you-partition-a-string-at-any-index-at-any-time-in-producing-a-scramble
# 对比最后一种稍微改良了一下，对长度为奇数的情况，用-index:来解决，避免了if else的判断，本质没有任何区别
#==============================================================================
# class Solution(object):
#     def isScramble(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         if len(s1) != len(s2):
#             return False
#         return self.helper(s1,s2)
#     
#     def helper(self, s1, s2):
#         if len(s1) == 0 or s1 == s2:
#             return True
#         index = len(s1) // 2
#         s1left = self.generateDic(s1[:index])
#         s1right = self.generateDic(s1[index:])
#         
#         s2left1 = self.generateDic(s2[:index])
#         s2right1 = self.generateDic(s2[index:])
#         
#         s2left2 = self.generateDic(s2[(-index):])
#         s2right2 = self.generateDic(s2[:(-index)])
#         
#         if s1left == s2left1 and s1right == s2right1:
#             if self.helper(s1[:index],s2[:index]) and self.helper(s1[index:],s2[index:]):
#                 return True
#         if s1left == s2left2 and s1right == s2right2:
#             if self.helper(s1[:index],s2[(-index):]) and self.helper(s1[index:],s2[:(-index)]):
#                 return True
#         return False
#         
#     def generateDic(self, s1):
#         dic = {}
#         for item in s1:
#             if item in dic:
#                 dic[item] += 1 
#             else:
#                 dic[item] = 1
#         return dic
#==============================================================================

#==============================================================================
# class Solution(object):
#     def isScramble(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         if len(s1) != len(s2):
#             return False
#         return self.helper(s1,s2)
#     
#     def helper(self, s1, s2):
#         if len(s1) == 0 or s1 == s2:
#             return True
#         index = len(s1) // 2
#         s1left = self.generateDic(s1[:index])
#         s1right = self.generateDic(s1[index:])
#         
#         s2left1 = self.generateDic(s2[:index])
#         s2right1 = self.generateDic(s2[index:])
#         
#         if len(s1) % 2 == 1:
#             s2left2 = self.generateDic(s2[index+1:])
#             s2right2 = self.generateDic(s2[:index+1])
#         else:
#             s2left2 = self.generateDic(s2[index:])
#             s2right2 = self.generateDic(s2[:index])
#         
#         if s1left == s2left1 and s1right == s2right1:
#             if self.helper(s1[:index],s2[:index]) and self.helper(s1[index:],s2[index:]):
#                 return True
#         if s1left == s2left2 and s1right == s2right2:
#             if len(s1) % 2 == 1:
#                 if self.helper(s1[:index],s2[index+1:]) and self.helper(s1[index:],s2[:index+1]):
#                     return True
#             else:
#                 if self.helper(s1[:index],s2[index:]) and self.helper(s1[index:],s2[:index]):
#                     return True
#         return False
#         
#     def generateDic(self, s1):
#         dic = {}
#         for item in s1:
#             if item in dic:
#                 dic[item] += 1 
#             else:
#                 dic[item] = 1
#         return dic
#==============================================================================