#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 19:29:59 2018

@author: zhangchi
"""

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for item in cpdomains:
            item = item.split(" ")
            count = int(item[0])
            item = item[1]
            if item not in dic:
                dic[item] = count
            else:
                dic[item] += count
            for index, i in enumerate(item):
                if i == ".":
                    term = item[index+1:]
                    if term in dic:
                        dic[term] += count
                    else:
                        dic[term] = count
        result = []
        for item in dic:
            result.append(str(dic[item])+" "+item)
        return result
    
s = Solution()
print s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])