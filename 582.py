#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 09:28:34 2017

@author: zhangchi
"""

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        dic = {}
        for a,b in zip(ppid,pid):
            if a in dic:
                dic[a].append(b)
            else:
                dic[a] = [b]
        if kill not in pid and kill not in ppid:
            return []
        result = [kill]
        temp = [kill]
        while len(temp) > 0:
            temp2 = []
            while len(temp) > 0:
                point = temp.pop()
                if point in dic:
                    temp2 += dic[point]
                    result += dic[point]
            temp = temp2
        return result
        
s = Solution()
print s.killProcess([1],[0],1)