#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:38:23 2017

@author: zhangchi
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left = 0
        up = 0
        down = len(matrix)
        right = len(matrix[0])
        direction = ["r","d","l","u"]
        index = 0
        result = []
        label = True
        # 获得坐标，之所以没直接把坐标用到matrix里获得值放到final list里，是为了方便这段代码以后复习
        while label:
            if index == 4:
                index = 0
            d = direction[index]
            index += 1
            label = False
            if d == "r":
                for i in xrange(left,right):
                    result.append((up,i))
                    label = True # 上次有更新，所以要进行后一次移动（r/d/l/u）直到没有更新了
                up += 1 # 最上层移动了，天花板就下沉了
            if d == "d":
                for i in xrange(up,down):
                    result.append((i,right-1))
                    label = True
                right -= 1
            if d == "l":
                for i in xrange(right-1,left-1,-1): #这么多-1只是因为配合python的循环特征
                    result.append((down-1,i))
                    label = True
                down -= 1
            if d == "u":
                for i in xrange(down-1,up-1,-1):
                    result.append((i,left))
                    label = True
                left += 1
        final = []
        for a,b in result:
            final.append(matrix[a][b])
        return final
        
s = Solution()
temp = [
 [ 1, 2, 3, 4 ],
 [ 4, 5, 6, 7 ],
 [ 7, 8, 9, 10 ]
]
print s.spiralOrder(temp)