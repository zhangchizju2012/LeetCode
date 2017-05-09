#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:39:43 2017

@author: zhangchi
"""

class Solution(object):
    # it works, but sames use list[list] is a better idea
    # 用多重循环替代recursion
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        lengthS = len(s)
        lengthT = len(t)
        result = [[0]*(lengthT+1) for _ in xrange(lengthS+1)]
        for i in xrange(lengthS+1):
            result[i][0] = 1
        for i in xrange(1,lengthS+1):
            for j in xrange(1,lengthT+1):
                # 先循环哪个后循环哪个根据具体情况具体分析，也可能有些题目这样循环不行
                if s[i-1] == t[j-1]:
                    result[i][j] = result[i-1][j-1] + result[i-1][j]
                else:
                    result[i][j] = result[i-1][j]
        return result[lengthS][lengthT]

#==============================================================================
# class Solution(object):
#     # it works, but sames use list[list] is a better idea
#     def numDistinct(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: int
#         """
#         result = {}
#         lengthS = len(s)
#         lengthT = len(t)
#         for i in xrange(lengthT+1):
#             result[(0,i)] = 0
#         for i in xrange(lengthS+1):
#             result[(i,0)] = 1 # change order, because (0,0) should be 1
#         for i in xrange(1,lengthS+1):
#             for j in xrange(1,lengthT+1):
#                 if s[i-1] == t[j-1]:
#                     result[(i,j)] = result[(i-1,j-1)] + result[(i-1,j)]
#                 else:
#                     result[(i,j)] = result[(i-1,j)]
#         return result[(lengthS,lengthT)]
#==============================================================================

#==============================================================================
# class Solution(object):
#     # it works, the same as lintcode 77, leetcode 72.
#     # however, recursion is not a good idea, the same problem also exists in 77 & 72.
#     def __init__(self):
#         self.result = {}
#     def numDistinct(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: int
#         """
#         lengthS = len(s)
#         lengthT = len(t)
#         self.s = s
#         self.t = t
#         for i in xrange(lengthT+1):
#             self.result[(0,i)] = 0
#         for i in xrange(lengthS+1):
#             self.result[(i,0)] = 1 # change order, because (0,0) should be 1
#         return self.helper(lengthS,lengthT)
#         
#     def helper(self,i,j):
#         if (i,j) not in self.result:
#             if self.s[i-1] == self.t[j-1]:
#                 temp = self.helper(i-1,j-1) + self.helper(i-1,j)
#             else:
#                 temp = self.helper(i-1,j)
#             self.result[(i,j)] = temp
#         return self.result[(i,j)]
#==============================================================================
                           
s = Solution()
print s.numDistinct("raabbbit", "rabbit")
        

#==============================================================================
# class Solution(object):
#     # wrong
#     # can't solve this problem: aacaacca & ca
#     # 把最后程序的最后几个变量print出来就知道是什么含义了
#     # 确实能解决"lllraebbbitlll","rabit"的问题
#     # 抓住前面的string肯定比后面的string要涵盖东西多的特点
#     def helper(self,m,n):
#         result = 1
#         for i in range(m,m-n,-1):
#             result *= i
#         for i in range(1,n+1):
#             result /= i
#         return result
#     def numDistinct(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: int
#         """
#         if len(t) == 0:
#             return 1
#             
#         previous = t[0]
#         vocab = []
#         countVocab = []
#         tempCount = 1 
#         for i in xrange(1,len(t)):
#             if t[i] == previous:
#                 tempCount += 1
#             else:
#                 vocab.append(previous)
#                 countVocab.append(tempCount)
#                 previous = t[i]
#                 tempCount = 1
#         vocab.append(previous)
#         countVocab.append(tempCount)
#             
#         countS = [] #每个数都应该比对应位置上的countVocab上的数大
#         start = 0
#         count = 0
#         for i in xrange(len(vocab)):
#             aim = vocab[i]
#             for j in xrange(start,len(s)):
#                 if s[j] == aim:
#                     count += 1
#                 else:
#                     # count == 0 是字母不同的多余的元素，直接删掉就好
#                     if count > 0:
#                         start = j
#                         countS.append(count)
#                         count = 0
#                         break
#         if count > 0:
#             countS.append(count)
#             
#         result = 1
#         if len(countS) < len(countVocab):
#             return 0
#         for i,j in zip(countS,countVocab):
#             if i < j:
#                 return 0
#             else:
#                 result *= self.helper(i,j)
#                 
#         #print countS
#         #print countVocab
#         #print vocab
#         return result
#==============================================================================
        
#s = Solution()
#print s.numDistinct("lllraebbbitlll","rabit")