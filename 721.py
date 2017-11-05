#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:49:51 2017

@author: zhangchi
"""

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dic = {}
        for item in accounts:
            if item[0] not in dic:
                dic[item[0]] = [set(item[1:])]
            else:
                temp = set(item[1:])
                tempList = []
                for i in xrange(len(dic[item[0]])):
                    # 有重复的都融合
                    if len(dic[item[0]][i].intersection(temp)) > 0:
                        temp = dic[item[0]][i].union(temp)
                    # 没重复的放一边
                    else:
                        tempList.append(dic[item[0]][i])
                # 合并
                tempList.append(temp)
                # 更新
                dic[item[0]] = tempList
                    
        result = []
        for name in dic:
            for item in dic[name]:
                temp = list(item)
                temp.sort()
                result.append([name]+temp)
        return result
    
s = Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print s.accountsMerge(accounts)
                        
                
                
                