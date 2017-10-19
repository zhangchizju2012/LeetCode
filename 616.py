#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:29:38 2017

@author: zhangchi
"""

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        temp = []
        for item in dict:
            if item in s:
                tempS = s
                index = tempS.find(item)
                before = 0
                while index >= 0:
                    #可能存在多个
                    temp.append([index+before,index+len(item)+before])
                    before = before+index+1
                    tempS = tempS[index+1:]
                    index = tempS.find(item)
        temp.sort(key=lambda x:x[0])
        if len(temp) > 0:
            #将能合并的东西合并，跟57一致，先写的616再写的57
            result = [temp[0]]
            for i in xrange(1,len(temp)):
                a,b = temp[i]
                if a <= result[-1][1]:
                    result[-1][1] = max(result[-1][1],b)
                else:
                    result.append(temp[i])
                    
            final = ""
            previous = 0
            for begin,end in result:
                final += s[previous:begin] + "<b>" + s[begin:end] + "</b>"
                previous = end
            final += s[previous:]
            return final
        else:
            return s
        
s = Solution()
print s.addBoldTag("aaabbcc",["aaa","aab","bc"])
            
                