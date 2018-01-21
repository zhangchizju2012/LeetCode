#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 20:08:25 2018

@author: zhangchi
"""

class Solution(object):
    # 先隔空放，换字符了，可以马上连下去，再继续隔空放，一轮放完了，剩下的空随便放
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        dic = {}
        for item in S:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        temp = []
        for item in dic:
            temp.append([item,dic[item]])
        temp.sort(key=lambda x:x[1],reverse=True)
        
        length = len(S)
        maxLength = (length+1) // 2
        
        if temp[0][1] > maxLength:
            return ""
        result = [0] * length
        
        point = 0
        label = True
        
        for item in temp:
            count = item[1]
            char = item[0]
            while point < length:
                result[point] = char
                count -= 1
                point += 2
                if count == 0:
                    point -= 1
                    break
            if label and point >= length:
                label = False
                left = []
                for index, item in enumerate(result):
                    if item == 0:
                        left.append(index)
                newPoint = 0
            while count > 0:
                result[left[newPoint]] = char
                newPoint += 1
                count -= 1
        
        return "".join(result)
    
    
s = Solution()
print s.reorganizeString("aaab")