#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 01:40:27 2017

@author: zhangchi
"""

class LogSystem(object):
    # 比赛的时候觉得烦懒得做，结果AC对算法复杂度要求很低，按照line25可以进一步优化的
    def __init__(self):
        self.dic = {}
        #self.list = []
        
    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        # 认为timestamp和id都是唯一的，要是不唯一的话dic的value搞成list的就好
        temp = timestamp.split(":")
        value = int("".join(temp))
        self.dic[value] = id
        # 这里还可以优化的，把所有的键都排好序弄成list，然后retrive的时候直接二分法去找所需的位置，
        # 避免搜索整个dict, 多添加一个方法，往list里加新元素和retrieve时查找初始位置时可以采用
        # 同一方法，别采用.sort()，不太适合这里
        #self.list.append(value)
        #self.list.sort()
        
    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        tempS = s.split(":")
        tempE = e.split(":")
        if gra == "Year":
            tempS[1] = "00"
            tempE[1] = '13'
        elif gra == "Month":
            tempS[2] = "00"
            tempE[2] = "32"
        elif gra == "Day":
            tempS[3] = "00"
            tempS[4] = "00"
            tempS[5] = "00"
            tempE[3] = "24"
        elif gra == "Hour":
            tempS[4] = "00"
            tempS[5] = "00"
            tempE[4] = "60"
        elif gra == "Minute":
            tempS[5] = "00"
            tempE[5] = "60"
        tempS = int("".join(tempS))
        tempE = int("".join(tempE))
        result = []
        for item in self.dic:
            if tempS <= item <= tempE:
                result.append(self.dic[item])
        return result
        
s = LogSystem()
s.put(1, "2017:01:01:23:59:59")
s.put(2, "2017:01:01:22:59:59")
s.put(3, "2016:01:01:00:00:00")
print s.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year")