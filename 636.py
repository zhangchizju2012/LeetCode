#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 19:36:22 2017

@author: zhangchi
"""

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stackId = []
        stackTime = []
        result = {}
        for log in logs:
            item = log.split(":")
            if item[1] == "start":
                stackId.append("shit"+str(int(item[0]))) # 这个很关键
                stackTime.append(int(item[2]))
            else:
                now = 0
                node = stackId.pop()
                while node.isdigit():
                    now += int(node) # 这个很关键
                    node = stackId.pop()
                startTime = stackTime.pop()
                if int(item[0]) not in result:
                    result[int(item[0])] = int(item[2]) - startTime - now + 1
                else:
                    result[int(item[0])] += int(item[2]) - startTime - now + 1
                stackId.append(str(int(item[2]) - startTime + 1)) # 这个很关键
        final = []
        for i in range(n):
            final.append(result[i])
        return final
        
s = Solution()
#a = ["0:start:0","0:start:1","0:start:2","0:end:3","0:end:4","0:end:5"]
a = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
#==============================================================================
# a = ["0:start:0",
#  "1:start:2",
#  "0:start:3",
#  "0:end:4",
#  "1:end:5",
#  "0:end:6"]
#==============================================================================
print s.exclusiveTime(2,a)