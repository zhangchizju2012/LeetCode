#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 08:06:53 2017

@author: zhangchi
"""

class Solution(object):
    # graph, dfs, 自己完成的
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dic = {}
        for start, end in tickets:
            if start in dic:
                dic[start].append(end)
            else:
                dic[start] = [end]
        for item in dic:
            dic[item].sort()
        # 第一次构建    
        result = []
        start = "JFK"
        while start in dic and len(dic[start]) > 0:
            temp = dic[start][0]
            result.append((start,temp,0,len(dic[start])-1))
            # 这里的减1是为了后面point[2] == point[3]这里不用减一，实际上的长度不应该减一
            dic[start] = dic[start][1:]
            start = temp
            
        length = len(tickets)
        while len(result) != length: # 这里是之前欠考虑的（也就是下面wrong算法里没有的）
            point = result.pop() # 改变越靠后的lexical order变动越小
            # 找到可以变动的点
            while point[2] == point[3]:
                dic[point[0]] = dic[point[0]][:point[2]] + [point[1]] + dic[point[0]][point[2]:] 
                # 把该放回的东西放回到字典里去
                point = result.pop()
            # 找到点之后按之前的流程重新走，第一个点append到result里稍微注意一下
            # 核心思想还是dfs, 找到可以动的点，然后选择另一个出发点
            start = point[0]
            result.append((point[0],dic[point[0]][point[2]],point[2]+1,point[3]))
            start = dic[point[0]][point[2]]
            dic[point[0]][point[2]] = point[1]

            while start in dic and len(dic[start]) > 0: # repeat as before.
                temp = dic[start][0]
                result.append((start,temp,0,len(dic[start])-1))
                dic[start] = dic[start][1:]
                start = temp
        final = []
        final.append(result[0][0])
        for item in result:
            final.append(item[1])
        return final

#==============================================================================
# class Solution(object):
#     # wrong
#     def findItinerary(self, tickets):
#         """
#         :type tickets: List[List[str]]
#         :rtype: List[str]
#         """
#         dic = {}
#         for start, end in tickets:
#             if start in dic:
#                 dic[start].append(end)
#             else:
#                 dic[start] = [end]
#         for item in dic:
#             dic[item].sort()
#         result = []
#         start = "JFK"
#         while start in dic and len(dic[start]) > 0:
#             result.append(start)
#             temp = dic[start][0]
#             dic[start] = dic[start][1:]
#             start = temp
#         result.append(temp)
#         return result
#==============================================================================
            
s = Solution()
a = [["CBR","JFK"],["TIA","EZE"],["AUA","TIA"],["JFK","EZE"],["BNE","CBR"],["JFK","CBR"],["CBR","AUA"],["EZE","HBA"],["AXA","ANU"],["BNE","EZE"],["AXA","EZE"],["AUA","ADL"],["OOL","JFK"],["BNE","AXA"],["OOL","EZE"],["EZE","ADL"],["TIA","BNE"],["EZE","TIA"],["JFK","AUA"],["AUA","EZE"],["ANU","ADL"],["TIA","BNE"],["EZE","OOL"],["ANU","BNE"],["EZE","ANU"],["ANU","AUA"],["BNE","ANU"],["CNS","JFK"],["TIA","ADL"],["ADL","AXA"],["JFK","OOL"],["AUA","ADL"],["ADL","TIA"],["ADL","ANU"],["ADL","JFK"],["BNE","EZE"],["ANU","BNE"],["JFK","BNE"],["EZE","AUA"],["EZE","AXA"],["AUA","TIA"],["ADL","CNS"],["AXA","AUA"]]
b = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print s.findItinerary(a)