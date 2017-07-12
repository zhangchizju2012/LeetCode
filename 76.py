#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 01:06:15 2017

@author: zhangchi
"""

class Solution(object):
    # 参考注释掉的那部分，那部分代码是假设t里没有重复的数，更方便理解，思路完全一样
    # 自己写的，估计能优化，现在只能击败15%（不过是hard题，能做出来不错）
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        dic_temp = {} # 用于确定t中所有的字母都已经满足要求，满足要求了之后就没用了
        count = len(t) # 配合dic_temp使用
        for item in t:
            if item not in dic:
                dic[item] = [float('inf')] # 因为一个字母可能需要多次，所以要记录出现多次的位置
                dic_temp[item] = 1
            else:
                dic[item].append(float('inf'))
                dic_temp[item] += 1
        head = float('inf')
        result = []
        for index, item in enumerate(s):
            if count > 0:
                if item in dic:
                    dic[item] = dic[item][1:] + [index] # 后面再次出现，之前出现过多的没有用（为了减少最后结果的长度）
                if item in dic_temp and dic_temp[item] > 0:
                    dic_temp[item] -= 1
                    count -= 1
                if count == 0: # 满足要求了，可以考虑head了
                    for thing in dic:
                        head = min(head, dic[thing][0])
                    #result.append((head,index))
                    result = [head,index] # 结果就是所有元素的最开头到当前的index
            else:
                if item == s[head]: # 新出现的字母跟之前的最开头的字母是同一个，说明现在这种情况也可以被考虑了
                    dic[item] = dic[item][1:] + [index]
                    head = index
                    for thing in dic:
                        head = min(head, dic[thing][0])
                    if index - head < result[1] - result[0]:
                        result = [head,index]
                    #result.append((head,index))
                else:
                    if item in dic:
                        dic[item] = dic[item][1:] + [index]
        if len(result) == 0:
            return ""
        else:      
            return s[result[0]:result[1]+1]

# 下面的代码是假设t里没有重复的数

#==============================================================================
# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         dic = {}
#         temp = set()
#         for item in t:
#             dic[item] = float('inf')
#             temp.add(item)
#         head = float('inf')
#         result = []
#         for index, item in enumerate(s):
#             if len(temp) > 0:
#                 if item in dic:
#                     dic[item] = index
#                 if item in temp:
#                     temp.remove(item)
#                 if len(temp) == 0:
#                     for thing in dic:
#                         head = min(head, dic[thing])
#                     #result.append((head,index))
#                     result = [head,index]
#             else:
#                 if item == s[head]:
#                     dic[item] = index
#                     head = index
#                     for thing in dic:
#                         head = min(head, dic[thing])
#                     if index - head < result[1] - result[0]:
#                         result = [head,index]
#                     #result.append((head,index))
#                 else:
#                     if item in dic:
#                         dic[item] = index
#         if len(result) == 0:
#             return ""
#         else:      
#             return s[result[0]:result[1]+1]
#==============================================================================
        
s = Solution()
print s.minWindow("A","AA")