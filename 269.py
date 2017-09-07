#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:22:29 2017

@author: zhangchi
"""

class Solution(object):
    # 有两种不存在结果的可能，一种是直接aba，一种是在一个地方ab,另一个地方ba
    # bfs的过程像topological sort
    # 没看答案，但是看到了bfs这个词，自己写的
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.label = False
        self.result = []
        self.helper(words)
        if self.label == True:
            return ""
        previous = {}
        future = {}
        left = set()
        for each in self.result:
            if len(each) == 1: # 可能会有多余的元素，先放在left里
                left.add(each[0])
            else:
                # 相当于构建topological sort的前后顺序
                for i in xrange(len(each)-1):
                    if each[i] not in future:
                        future[each[i]] = set([each[i+1]])
                    else:
                        future[each[i]].add(each[i+1])
                    if each[i+1] not in previous:
                        previous[each[i+1]] = set([each[i]])
                    else:
                        previous[each[i+1]].add(each[i])
        noRequireSet = set(future.keys()).difference(set(previous.keys()))
        returnResult = ""
        
        while len(noRequireSet) > 0:
            temp = set()
            for item in noRequireSet:
                returnResult += item
                # 满足要求的及时pop走，为line56做准备
                if item in future: # 可能已经被pop走了
                    for popitem in future[item]:
                        previous[popitem].remove(item)
                        if len(previous[popitem]) == 0:
                            previous.pop(popitem)
                            temp.add(popitem)
                    future.pop(item)
            noRequireSet = temp
        if len(future) > 0 : #第二种不存在结果的可能
            return ""
        else:
            for item in left:
                if item not in returnResult:
                    returnResult += item
            return returnResult
    
    def helper(self, words):
        if self.label == False:
            temp = []
            dic = {}
            for index, item in enumerate(words):
                if item[0] in dic and item[0] != words[index-1][0]:#第一种不存在结果的可能
                    self.label = True 
                    break
                if item[0] not in dic:
                    temp.append(item[0])
                    dic[item[0]] = []
                if len(item) > 1:
                    dic[item[0]].append(item[1:])
            #if len(temp) > 1: #只有一个的没有有用信息，错！但是可能有新的元素
            self.result.append(temp)
            for item in dic:
                if len(dic[item]) >= 1: #有些虽然只有一个，但是能有新的元素
                    self.helper(dic[item])

# 未考虑不存在的情况
# =============================================================================
#     def alienOrder(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         self.result = []
#         self.helper(words)
#         previous = {}
#         future = {}
#         for each in self.result:
#             for i in xrange(len(each)-1):
#                 if each[i] not in future:
#                     future[each[i]] = set([each[i+1]])
#                 else:
#                     future[each[i]].add(each[i+1])
#                 if each[i+1] not in previous:
#                     previous[each[i+1]] = set([each[i]])
#                 else:
#                     previous[each[i+1]].add(each[i])
#         noRequireSet = set(future.keys()).difference(set(previous.keys()))
#         returnResult = ""
#         
#         while len(noRequireSet) > 0:
#             temp = set()
#             for item in noRequireSet:
#                 returnResult += item
#                 if item in future: # 可能已经被pop走了
#                     for popitem in future[item]:
#                         previous[popitem].remove(item)
#                         if len(previous[popitem]) == 0:
#                             previous.pop(popitem)
#                             temp.add(popitem)
#                     future.pop(item)
#             noRequireSet = temp
#         return returnResult, self.result, previous, future
#     
#     def helper(self, words):
#         temp = []
#         dic = {}
#         for item in words:
#             if item[0] not in dic:
#                 temp.append(item[0])
#                 dic[item[0]] = []
#             if len(item) > 1:
#                 dic[item[0]].append(item[1:])
#         if len(temp) > 1: #只有一个的没有有用信息
#             self.result.append(temp)
#         for item in dic:
#             if len(dic[item]) >= 2:
#                 self.helper(dic[item])
# =============================================================================
                
s = Solution()
a = ["ab","adc"]
#a = ["z","z"]
# =============================================================================
# a = [
#      "a",
#   "zx",
#   "zz",
#   "x"
# ]
# =============================================================================
# =============================================================================
# a = [
#   "z",
#   "x"
# ]
# =============================================================================
# =============================================================================
# a = [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# =============================================================================

print s.alienOrder(a)
                    