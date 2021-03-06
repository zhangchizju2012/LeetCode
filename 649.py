#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 20:47:47 2017

@author: zhangchi
"""

# 最优的策略就是让后面离自己最近的对手失去所有权利
# 记录R/D的个数，不断地扫描，更新senate
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        count = 0
        value = None
        changedSenate = []
        while True:
            for item in senate:
                if count == 0:
                    value = item
                    count += 1
                    changedSenate.append(item)
                else:
                    if item == value:
                        count += 1
                        changedSenate.append(item)
                    else:
                        count -= 1
            if len(senate) == len(changedSenate):
                if senate[0] == "R":
                    return "Radiant"
                else:
                    return "Dire"
            else:
                senate = changedSenate
                changedSenate = []

s = Solution()
#a = "RDDDRRRRDRRRRDRRRRDDDRDDRRRRDDRRDDRDDDDRDDDDRDRRRDRDDDRDDRRRRRRRRRRDRDDRRRRDRRDDDRRRRDDRDRDRRRDRDDDRDDDDRRRDRDDDRDDRDRDDRDDRDRRDRDRDDRRRDRRRRRDRDDRDDRRRDRDDRDDRDDRRDDDRRDDDRDRRDRDRDDDDDDDRDDRRDDDRRRDRDRDRRRDDDRDRRDRDDRRRRDDRRRRRDDRRDRRRRDRDDDDDDDRDDRDRRDRDRDDRRRRDRDRRRRDDRDDDRDRDRRDRDRDRDRRDDRRRRRDRDRDDDDDRRRRRRRDDDRDDDDRDDRDRRDRRDRRDRDDRDDRRDRRRDRDDRDDDRDDRRDDRRDRDRDDDDDRDRDRDRRRRRRRDRRDRDDRRRDDDDDRRDRDRDDDRRDDRDDDRRDDRRDDDDDDRRRDRRDRRDDRRRDRDDDRRRDRRDRRDDRRDRRRDRRDDDDRDRDRDDDRRRDDDRRRRDDRDRDRRDRRDRRDRDRRRDRDDDDRRRRRRDDDDRRDDRDDDDDDDDRRDRDRDDDRRRDDRRDRRDRRDRDRDRRRDRRDRDRRRRRDDRDRRDDDDRRRRDRRDRRDDRDDRRDDDRRRDDRDDDDRRDRRRRRDRDRRDDDDDDRRDRDRRDDDRDDDDDRDRDDDRDRRRDRRRDDDRRRDDRDRRRRDDDDDRDRRRDDDDRDDDRRDDRRRRRDRRDRRDRDRRDRDDDRRRDDDDDRDRDDDRRDRRRRRDDRRDRDRDRDDRDDRRRDRRDRRDRDRDDRRRDRRRDDRDRDRDDDDDDRDDRRDRRRRDRRDRDDDDDRRRDRDDDRDRRDRDRDDRRRRRDDRRDDDRDDDRRRRRRRRDDDRDDDDDRDDRRDDRDDDRRRDRDRDRDRDDRDDDDRRRDDRRDDDRRDDDRRDDRDDRDDDDRDDDDRDRRDDRDDDDRRDRRDDDRRDRDRRDDRDRRRRDDDDRDRRDRDDRRDDDRDRRRDRRDDDRDRDRDDRRRDRDDRRRDRRRDRDRRRRDDRRRDDRDDRDRRRDDRDRRDDRDDDDDRDDRRRRRRRRRDRDRDRRRDRDRRRRRDDDRDDDDDDRRDDDRDDDDDDRDDDRRRRRRDRRDRRDRRRRRDRRRRDDDDDRRRDDRRDDRRDRRRDDRRRDRDRRRRDRDRRRRRRDDRRRDRDRRDRRDDDRRDRRRDRRDDDDDRRDDDDRRDRDRRRRDRDRRDDRRRRRRRRRDDRDRDRDDRRRRRDDRRDRDDDDDRDDDRRDRDRDDRDDRDDDRDRDRRDRDRRRDDDDDDRRRDDRRDDRRDDDDRRDRRRDDRRRRDRDRRDDDDRRDDDRDDRDRDRDDDDRDRDRRDRRRRDDRDDDDDDDRDRRRRRDRDRDRDDDDRDRDDRDRDDDRDRDDDDRRRDRDDDDDDDRDRDRDRRDRRRRDRRRRRDRRDRRDRRDDDDDRRRDRDRRRDRDRDRDDDRRDRRRDDRRDRRDDRRDDRRRRRDDRDRDDDRDDDDDDRRDRRDRRDDDDDRDRDDRDRDDDDRDDDDRRDRRRDRRRRDRDDRDDDRDRRRDRDRRRDDDRRRDRRDDDRRRDRDRDRDRRDDDDDDDDRDRRRDDRRRRRRDRDDDRRDRDDDDDDRDDRDRRDDRDDRDDDRDRDRRRRRDDRRRDDDDRRRRRRRRRDRDDDRDRDDDDDDRDDDRRDRDRRDDRRDDRRRRRRDRRRRDRRRDRDRRDRDDRDRRDDDDRRRDRDDDRDDDDDRDRRDDRRDRRRRDRRRRDRDRDDRRRRDDDDDDDDRDRRRRDRRRRRDRDRDDDDDRRDDDDDRDDRRRRRRRDRDDRRDRRDDRDRDRRDDRDRDRDRRDDDRDRDRDDDDRRRRRDDDRDDDRDRDDDRDRDRDDRRDRDDRDRDDDDDDDDDRDDRRRDRRDRRRRDRDRRDRRDRDRRRDDRDDRDRRRDDDRDRRRRRRDRRRRRRDRRDDDRRRRDDDDRRRDDDDRRDRRDDRDRRRDDRDDDDDDDRDDRRDDDDRRDDRRDDDRRDDRDDRDDDDRRDDDDDDRRRRRRDRDDRRDRRRDDDDDDRRDRDDRRDDRDRDRRRRRDRDRRRRRDDDRRRDRDRDDDRDRDRRRDRDRRRRRDDDRDDRRRDDRDDDDDRRRDDRDDDDRRDDDDDRDDRRRRDRDDDDDDDRRRRDRRRDRDDDDDRDRRDDRRRRDRRDRDDDDDDRDRRRRDRRDDDRRDDDRRRDDDDDRDRDDRDRDRRDRDRRRRDRDRRRDDRRDRRRRDRRDDDRDDRRDDDDDDDRDDDRDRDDRDDDDRDDRDRDDRDDDDRDDRDRRRDRDRDDDDRDDRRDDRRRDDRRDRRRRRRDRRDDRDDRRDDRRRRDRRDRRRRRDDDRDRDDRDRDDRDDRDDDDDRDDRRRRRDRDDDDDRRDDDRRRRDDRRRDRRDDDDRDRDDDDDDRDRRDDRDRRDRRRRDRDRRDDRRDRDDDRDRDRDRDRDDDRDRRDRRDRDDDRRRDDRDRDDRRRRDRRDDDDDDDDDDRRDRDDDRDRDDDRRRRRDRRRDRRDDRRRRDDDDRRRRRDDDDDRDDRRRRDDDDDDRDRDDRDRRRDRRRDRDRRRRDDDRRRDRDDRRDRDRDDRRDDRRDDRRRDDDDRDDDRRDRRRDRRDDDRDDRRDRDDDRDRRDRRRRDRDDDRDRDDDRDRDDRDDDDDDRDRDRDRDRRDDDDDRDDDDDDDRDDRDDRDRRDDDRRDRRRDRDRDRRDRRDRDRDDDDDRDDRDRRDDDRDDDDDDRDRRDDRRDRRDRRRDDRDDRRDRRDRDRDDRRRDDRRRRRDDDRDRRDRRRDDDDRDDDDRDDRRDRDDDDDDDDRDRRDDRDDRDDDRDRDRRDRRDRRRDDDDDDDDRDDRRDDDRDDDRDRDDDDDRDDDRRDRRRRDRRDRDDRRRRDRRRRRDDDRDDDDRDDRRRRRDDRRRDDRRDDDRRDDDDDDRRRDDDRRRRDRDRDDDRRRRDDDRRDRRDDRDRDDDDDRDRRRRDRRDDRRRRDRDDRRRRRDRDDRRRRDRDRDDRRRRDDRRDRRRDDDRDRDRRRDRDRRRDRRRDDDRDRDRRRDRRDRRRRRDDRDDDRRRRDDDRRDRDRDRRDDRRDRRDRDDDDDRRRDRRRRRDDRRDRDRDDRRRDDRRRRDRDRRDDRDRDRDRDRDRDDRDRRRDRRDRDRRRRDDRRDRDRRDRRRRRDDDRDRRDDDRDRRDDRRRRDDRRRRDRDDRDDRDDDDDDRDRRDDDDRRRRRRDDDDDRDRDRRRRDRRDDDRDRDRDRRDDRDDDRDRRDRRRDRRRDRRDDRRDRRRDRDDDRDDDRDRDRRDRRDDRRDRRRRRRDRRRDDDRDRRRRDRRRRRDRDDRRRDRRRRDRRRRRRRDRRRDDDRRRDDDRRRRDDRRRRRDRDDDRRDRRDDRRRDRDRDRRRDRDDRRDDRDDDDDDDDRRDDRRRRRRRDRDDDDDRDDDRDDRRRDDDRDDDRRRDDRRRRRRRRDRDRRDDDRRDRRRRRDRRDDRDRDRDDRRRRRDRDDDRRDRDRRRRRDDRRRDRRRDRRDDRDDRRDDRDDRRDDDDRRDRDRDDRRDRRDDRRRDDDRDRRDRRRRRRDDRRRRRRDDDRRDRDDDRRRDRDRRRRDRRDRRRRRDDDDDRDDRDDDRDRDDRDDRRDRRRDDRDDRRRDRRRDDRRRDRDRRRDDDRRDRDRRRRRDDRRDDDRDRRRRDDDRRRRRRDRDRRRDDDRDDDDDRRDRDDRDDDRRRRRRDRRRDDRDRDDRDDRDDRDDRRDRDDRRDDRDRRDDDDRDRDRDRRDRDDDRRDDRDDRDDDDRRDRDDDDDRRRRDDDDRDDDDDDDDRDDRDDRRDRRRRDDRRRRDDDRDRRDDDRRRRRRRDDRDDRDDRDRRDDRRRRDDDDDRRDDRRDDDRRRDRDDDRRRRRDDDDDRDRDDRRDDDDDRDDRRDDDDRRRDDDRRDDRRRRRDRDRDRRRDRRDRDDRRDDRRRDRRDRDRDRRDDRDDDRDDDDDDDRRRRDDRDRRDRRRDDRDRRDDDDRRDDRDRRRRRDDDDRRDRRDDDRDDDDDDRRRDDDRRDRRDDDRRDDDDDDRRRDRDDRDRRDDDDDDDRDDRDDDRRDRRRRRDDDDRDDDDDDRRRRDDDRRRDDRDRRDDDRRRRRRRDRRRRDRDDDDDDDRRDRDDDDDRRDRDDDDRRRRRDRDRRDRRDDDRRRRDDRDDDRRRDRDDDDRRRRRDRRDDRDRRRDDDDDRRRDDRRDRRDRRRDRRDRRDDRDRDRRDRRDDRDDDRDRDDDDDRRDDDDRDRDRRDDDDDDDDRRDDRDDDRDDRDDDDDDDRDRRDDDRRDRDRRRRRDRDDRRRDRRRRDDRDDRDRDDRDRRRRDDDRRRRDRDRRDRRRRRDDDDRDDRDRDRDRDRDRDRDDDDDDDDDDDDRRDDDDDRRRDRDRRDDDRDRDDRRDRRRRRDDDDRDRDDDDRDRDRDDRRRRDRDDRDDDDRDRRDRRRRDRDRDDDDRDDDRDRDRDRRRRDRDRRDDRRRDRRDDDRRDRRRDDDRRRDRDDRDDRRRRDDRRRRDDRDDRRRDDRDDDRDDRDDRDRDRRDRRRDDRRRDRDDRRDDDDRRDRDDRDRRRDDRRRDRDDRDDDDRRDDRRRDRDDDRRRDRRRRRDRDRDRDDDRRDDRRDRRDRDDDRRDDRDRDDRRDRDRRRDRDRDRDRRDRRDRRRRDDDRDRRDRDDDRRDDDDRDDRRRDDDRDDRRDDRDDRRRDDRDRDDDRRRRDRRDDDDRRDDDRDRRDRDRRDDDRDDDRDDDRRDDDRDRRRRRRDDDDDDDRRDRDDDRDRRRDRRRRDRDRRRDDDDRDDDRDDDDRRRRDDDDDDRDDRRRDDRRRDRDDRDDDRDDRDDDDDDRRDDDRDDDDRRRRDRDDDDDRRRDRRRRRDDDDRDRDDRRDDRDRRDDDRDRDDRDDDRDRDRDRRRRRRRRRRDDDDRRDDDRDDDRDDRDDDDRRRRDRRDDRRRRRRDRRRRRDRDRRRRDRRDDRRDRDRRRRDRDRRRDDDDRDDDDDRRRDDRDDRDDDRRRRDRDRDDDDRDDDDDDRDRRRRDDDDRDDDRRRDRRDDDRDRDRDDDDRDDRRDDRRRDDDDRRRRDDDRDDRRRDRRRRDRDRRDRRRRDDRRDRRDDRRDDDDDRRRDRDRRRDDDDDRDDDRRRRRDDRRDRRRRDRRRDDDRDRRDRDRRDRDDDDRDDRRDDRRDRRDDRDDDRRDDDRRRDDDRRDDRDDRRDRRRRDRRRDRRRRRDRDDDDDDRRRDDRRDRRDDRDRRDDRRDRRDRRDRDRRDDDRRDRDDDRRDRRRDRRDRRDRDRRRRDRRRRRRRRDRDDRRDRDDRRRDRRRDDDDDDRDDRDDDRRRDDDRRRRRDDDRRRDDRRDRDRRDRDRDRRDRDRDDDRRRRDDDRDRRRRRDRRDRRRDDRRDDRRDRRDRDRRDDRDDRRRRRDRRRRDRDRRRRRRRRDDRRRRDRDDRDDRDRDRRRDDRDDRDDRRRRRRRRRRDRRRDDRRDRRRRRRRRRRRDDRRDDRDDRDRDRRDRRDDDRDRDDDRDRRRRRDDDRRRDRDDRRDRDRRDDDRDRDRDRRDRRDDRRDRRDDRRRDRRRRDRDDRDRDRRDRDRRDDDRDRRDRRRDRDRDDRDDRDDRDRRRRRDRDRRDRDDDRRDRRRRDRRDDRRRRRRRDDRRDDDRDDRDRRRRDDRRDDRRDRDDRDRDDDRRRDRDRRRRDRRDRRDRRRRRRDRDDDRRRDDRRDDRDDRRRDRDRDDDRDDRRRDRDDRRDRDDRDRDDRRRRRRRDRDRRRDDRRRDDRDDRDRDRDDDDRDDRDRDDDDDDRDRRDDRRDDDRRRDDRRRDRRRDDRDRDDRDRDDDDRDDRRRRRDDDDRRDDRDRRDDDRRRDRRDRRRRRDDRRRRDDRDRDDRRDRRDDRRDRRDDRDDRRRDDRRDRRDRDRDRRDDDDRDRDDRDRDRDDDDDRDDDRRRDDRDRRRRDDRDDDRRDDDDDRRDDDRRRDRDDRDDDDRRRDDDDDRRRDDDDRDDDRRRRRRRRRDRDRRDRDDRRDRDRDRDDRRRRDDRRRRRRDRRRRDRDDRDRDRDDDDDDDRDRDDDRRRRRDDDRRRDDDRDDDDRDDRRRRDDDDRRDDRRDRRDDRRDRRDDDRRDRRRDDRRRDRRDRRRDRRRRRRDDDRRRDDRRDDDRRDDRRRDRDDRRRDRDDDRDDDRDDDDRRRRRRDDRRRDRDRRDRRRRDDRDDDDRRRRDDRDRDRRDRDRDDRRRDRRRDRDRDDRDRRDRDRDDDDDDDDRRDRDDRRRDDRRRRDRRRRRDRDDDDRRRRDDRDRDDRRRDDRDRDRRDRDRRDRRRDDRRRRRDRRDRRDRDDRDRDDRRDRDDDDRRRDRDRRRDDRDRRDRDRRDRRDRRDRDRDRDRRDDRRRDDRDDRDDDRRRRRRRDDDRRDRRDRRRRDDRDRDDRDDRDRRRDDDRDDRDDRDRRRDDDDDRRRDDDRDRRDRRDRRDRRDRRDRRDDDRRDDDRDDRRRDDDDDDRDDDRDRRRRDRDRDRDRRDRRDRRRDDDRDDRDDRDRRDRDRRRDDRRRRDRDRDDRRRDDDDDRDDDRDRDDRRDDDRRDRRRDDDRRRRRRDRRRRRDRDRDRDRDRRRRRRRDRDRRDDRDDDRDDDDRRRDRDRRDRDRDRRRRRDDRRDRRDDRDDRDRDRDDDDDDRDDDRDRRDDRDRRDRDDDDRDDDDDRDDRDRDRRRDRDDRDDRRRRDRRDDDRDRDRRRRRDRRRRRDDRDRRRRRRDDRRDRRDDDDRRDRDRDDDRRRRRRRDRDDRDDRRRDDRRDDRDDRDRDDDDDDRRDDRRDRRDRDRDRDRDRDDDRDDRDRRDRDRRRDRRRDDRRRDDRRRRDRRRRRRDDRRDRDRDDDDDRRDDRRRDDDRRRRDRDRDRRRDDRRDDDRDDRDRRDDRDRRDDRRRRRRDRDDDRDRRDDDDDDDRDDDDDRRRRDRDDRDDDRDRRRRRRRDDDDDDRDDRDRDRRDDDRDDRRRRRDDRDDDDRRRDRRDDRDDRDDRDDRDDRDRRRDRDDRDRRRRRDDDRDDRDRDRDDRDDRDRDRRDDRDRRRDDRRRDRRRRRRDRRDDDRDDDDRRRDRRDDDRRDRRRDDRRRDRDDRDDRDDRRDDDRRRDRDRDDDDRRDDRDDDDRRDDDRRDRDDDDRRDDRRRDRRRDDRRRDRDDRRDRRDRDDDDDRDRRDRRRDRRDDDDDRRDDRDRRDRRRRRDDDDRRRDRRRRDDRRDRDRDDDDDRRRDDRRRDDRRDDRRDRDDRDDRRDRDDDRDRDDRDDDDDDDDDDRDRDRRDDDDDDRDRDDDRDRRDDRRDRDRRDRRRDRRDDDDDDDRDDDRRDRRRRDDDDDDRRDDRDRDRRDDRDRDRDRRDRDDDDDDRDDRRDDRDDDRDRDRDDDDRDDDRRRRRDRDRRDRDDDRDDRRDDRRRRDDDRDRDRRRRDDRRDDDRDRRDDDDDRDDDRRDRDDDDRDRDDRDDDRRDRDRDDDRRRDRRRRDRDRDDDRDDDRRDDRRRRDRRRDRDDDDRRDRRDRDDRDRRRDDRDRRRRDRRRDRRRDRRDDRRDRDDDDDDRDDDDRRDRRDDDRDRRDDDRDDDDDDDRDDRDRRRDRRRRDRRDDDDRRRRDRDDRRDDDDDRDRDDRRDDDRRRDDDDDDRRRDDDRDDDDDDRDDRDRDDRDRDDRRRRDRRRRDDDRRDDRRDRDDRDRDRRDDDDDRDDRDDDRDDDDRDRDDRRRDDDDRRRDDRRDDRDRRDDRRDRRRDRDRRRDRDRRDDRDRDRDDRDRDRDRDRDRDDDRDRDDDDDRRDDRDRRDDDRDRRRDDRRDRRRRRRDDRDDDRRRDDDRDRRRDDRDDDDDRRRDRDDRRRDDDDRRRRDDRDRDRRDRDRRDRRRDRDRRDRDRDDDRRRDDDRRRRRDRRDDRRDDDDDDDRDRDRDDDDRDDRRDDDRDRDDDDDRRRRRDRDRDDDRRRDDDDRDDRDDDDDDDDRRDRRRDRRRRRRDRRRRDDDRDDRDRRRDDDDRRDDRDDRRRDDRRDRRDDDDRDDDDRRRRDRRRDRDRRDRDDDRDRDDDDRRRRRDRDRDRRRDRRRDDDDRDRDDRRRDDDRRRDDDDRDDRDRDRDDRDDDDDRDDRRRRRDRRDRDRDRDRDDDDRRRDRRRDDDDDDRRRRDRRDRRRDRDRRDRDDRRDRRDDDDRRRRDDRDRRDRDDRDRRDRDRRRDRDRRDDDDDDRDDRRDRDRDRDDDRDDDRRRDRRDDDRDDRRDDDRRDRDDRRDRDRRDDRRDRRRDDRRRRDRDDDDRDRRDRDDDRRRRDDDRRDDRRDDRRDRRDDRDRDRRDDDRDRDRDDDRDDDRRDRDRRRRRRRDRRDDRRDRRRRDRDDDDRDDRDDRRDRDDRRRDDDDRDDRDRDDDDDRRRDRDRRRRDRRRRRDDDRRRDDRDDDRRRRDDRRDRRDRRRDDDRRDRDDDDDDDDRRRDDRDRRDRDRRRDDDDRDDDDRRDRDDRRDDDRRRDRDRDRRDRDRRRDDRRDRRRDRDRRDRRDDRRRDDRDDDRDRDRDDRDRRRDDRRRRRRDDDRDDRRRRRRRRDRRDDDDDRDDRRRRDDDDRRRRRDDRDDRDDRRDRDRDDRDRRRDRRRRRRRRDDDDRDDDDRRDDRDDRDRDDRRRRRDDDRRRRRDRRDRRDDRDDDRDRRDDDRRDDRDDDDDDRRRDDDDDRRRDRDRDRDDDRDRRRRDDRRDDRDRRDDRRRDRRDDRDRRDRRDRDRRDRRDDDDDDRDDRRDRRRRRRDDDDRDRRDDRDRRRRRRDDRDDRDRDDRRRDRDRRRRDDRRRDDRDDRDDDRDRDRRRDDRDRDDDRRDDDRDDRDRRRDDDRDRRDRRRDDDRDDDRDRDDRDRRRDRDDRRDDDRDRRDDRRRDDRRDDDDDRDRDDDDDDRDRDRDRRRDRRDDDRRRDDRDRRDDRDDRDRRDRDRRDRDRRDDDRRDDDDRDDRDDDDDDRRRDRDRDRDDDDDDDDRDDRRRRRDDRDDDRDDDDRDRDRDRRDRRRDRRDDDRRRRDDRRRDDRDRRDDDRRRRRDRDRRRRDDDRDDDDDDDDRRRDDRRDRRRRDDRRDRRDDRDDRDRRDRRDDDRRDRDRDRRRRDRRDDDRDDRRDDRDDRRRRDRRRDRRDDDRRDDRDDDRDDDRDRRDDDRRDDRDRRRDRDRDDRDRRRDRRRDDDRRRDRRRRRDRDRRRRRRDDRDRRRRRRDRDRRDRDDDRDDDDDDDDDRRRDDDDDDDDDDDRDDDRDDRRDDRDDDDDRRDRDDDRRDRDDDDDRRRRRRRRDDRDDDRDRRRRRDDRRRRDDRRRDDRDRRRRDRDDRDDDRDDRRRRDRRRRRDRRRDDDDDRDRRDDRDRDDDDRRRRDDDRRRDRRDDRDRDRDRDRRRDRRRDDDDDRDDDDDRRRDDRDDRDRRDRDDRRDDRRRDDDDRDRRRDDRRDRRRDDDDDDDRRDDDRDDRDRRDDRDDDRRRDDDRDRRDRRDDDDDRDDRRDRRDDDRRDDDRRDRRDDDRRRDRRDRRDDDRDRDDDRDRDRDRRRDDRDDDRDRDRRDDRDRDRRDRDDRDDDDDDDRRDDDDRRDDDRRDDDDRRRDDRRDDRRDDRRRRDDDRDRDRRDDRRDDRRRDRDDRDRRDDRRRDDDDRRRDRRRRRDDRRRRRRRRDDDRRRDRRDDRDDRRRRRRRRRDDRRDRDRDDDDRDRDRRRDDRDDRDRRRDDDRDRDDRRDRDDDRRDRRDRDRRRRRDRDRDDDDDDDDRRDRRRRRRDRDDDDRRDRRRRDDRRDDRRRDDRRRDDDDRRRDDRDRDDDDDDDDRDDRRDDDRDRRRDRRDRRDRDRRRDDRDDRRRDRDRRDRDRRDDRRRRRDRRRDDRRDDDDRRDDDRRRRDDRDDRDDDDRDRRDRRDRDRDRRDRDRDDDDDDDDRDRDRRRDDRDRRRDRRRRDDRRRDDDRRDDDRDDRRDDDDRRRRDDDDRDRRD"
a = "D"
print s.predictPartyVictory(a)

# 后面的方法用了recursion，序列过长会让stack爆掉，思路也是可以的
# 后面的方法思路都是一样的，就是不断在优化，可以直接看最下面的，思路最直接

#==============================================================================
# class Solution(object):
#     # maximum recursion depth exceeded while calling a Python object
#     def predictPartyVictory(self, senate):
#         """
#         :type senate: str
#         :rtype: str
#         """
#         self.indexList = [i for i in xrange(len(senate))]
#         self.senate = senate
#         return self.helper(0)
#     
#     def helper(self, start):
#         if start >= len(self.indexList):
#             start -= len(self.indexList)
#         begin = self.senate[self.indexList[start]]
#         index = None
#         for i in xrange(start+1,len(self.indexList)):
#             if self.senate[self.indexList[i]] != begin:
#                 index = i
#                 self.indexList = self.indexList[:i] + self.indexList[i+1:]
#                 break
#         if index is None:
#             for i in xrange(0,start):
#                 if self.senate[self.indexList[i]] != begin:
#                     index = i
#                     self.indexList = self.indexList[:i] + self.indexList[i+1:]
#                     break
#                 
#         if index is None:
#             if begin == "R":
#                 return "Radiant"
#             else:
#                 return "Dire"
#         else:
#             return self.helper(index)
#==============================================================================
        
            
#==============================================================================
# class Solution(object):
#     def predictPartyVictory(self, senate):
#         """
#         :type senate: str
#         :rtype: str
#         """
#         if len(senate) == 1:
#             if senate[0] == "R":
#                 return "Radiant"
#             else:
#                 return "Dire"
#         self.dic = set()
#         self.senate = senate
#         for i in xrange(len(senate)):
#             self.dic.add(i)
#         return self.helper(0)
#     
#     def helper(self, start):
#         begin = self.senate[start]
#         index = None
#         for i in xrange(start+1,len(self.senate)):
#             if i in self.dic and self.senate[i] != begin:
#                 index = i
#                 self.dic.remove(index)
#                 break
#         if index is None:
#             for i in xrange(0,start):
#                 if i in self.dic and self.senate[i] != begin:
#                     index = i
#                     self.dic.remove(index)
#                     break
#                 
#         if index is None:
#             if self.senate[start] == "R":
#                 return "Radiant"
#             else:
#                 return "Dire"
#         nextIndex = self.findNext(start)
#         if nextIndex is None:
#             if self.senate[start] == "R":
#                 return "Radiant"
#             else:
#                 return "Dire"
#         else:
#             return self.helper(nextIndex)
#         
#     def findNext(self, start):
#         for i in xrange(start+1,len(self.senate)):
#             if i in self.dic:
#                 return i
#         for i in xrange(0,start):
#             if i in self.dic:
#                 return i
#         return None
#==============================================================================
        

#==============================================================================
# class Solution(object):
#     def predictPartyVictory(self, senate):
#         """
#         :type senate: str
#         :rtype: str
#         """
#         return self.helper(senate)
#     
#     def helper(self, senate):
#         if len(senate) == 1:
#             if senate[0] == "R":
#                 return "Radiant"
#             else:
#                 return "Dire"
#         begin = senate[0]
#         index = None
#         for i in xrange(1,len(senate)):
#             if senate[i] != begin:
#                 index = i
#                 break
#         if index is None:
#             if senate[0] == "R":
#                 return "Radiant"
#             else:
#                 return "Dire"
#         else:
#             return self.helper(senate[1:index]+senate[index+1:]+senate[0])
#==============================================================================
