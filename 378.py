#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:25:09 2017

@author: zhangchi
"""
import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        point = [0] * n
        result = []
        count = 0
        heap = []
        label = [False] * n
        # it makes more sense after draw the picture
        # only put real candidate in the heap list
        # but actually it's not fast
        # May due to too many if sentences
        heapq.heappush(heap,(matrix[0][0],0))
        label[0] = True
        point[0] += 1
        while count < k:
            value, position = heapq.heappop(heap)
            label[position] = False
            result.append(value)
            count += 1
            if point[position] <= n - 1 and (position == 0 or point[position-1] == n or point[position] < point[position-1]-1):
                heapq.heappush(heap,(matrix[position][point[position]],position))
                point[position] += 1
            if position != n - 1 and point[position+1] <= n - 1:#has bug here, some candidate shouldn't be add here.
                heapq.heappush(heap,(matrix[position+1][point[position+1]],position+1))
                point[position+1] += 1
        return result
    
    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # This is the fastest and right
        # 其实就是靠heapq来排序
        n = len(matrix)
        point = [0] * n
        result = []
        count = 0
        heap = []
        # it should be able to become more fast, but seems make it become complicated
        # stupid initilization
        for i in range(n):
            heapq.heappush(heap,(matrix[i][0],i))
            point[i] += 1
        while count < k:
            value, position = heapq.heappop(heap)
            result.append(value)
            count += 1
            if point[position] <= n - 1:
                heapq.heappush(heap,(matrix[position][point[position]],position))
                point[position] += 1
        return result

    def kthSmallest3(self, matrix, k):
        # draw a picture and understand why
        
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        point = [0] * n
        result = []
        count = 0
        while count < k:
            temp = float('inf')
            previous = None
            position = None
            for i in range(n):
                # compare again and again, make it become slow, so it comes heap
                if point[i] < n and point[i] != previous:
                    if matrix[i][point[i]] < temp:
                        temp = matrix[i][point[i]]
                        position = i
                    previous = point[i]
            result.append(temp)
            point[position] += 1
            count += 1
        return result[-1]
    
s = Solution()
a = [[1,1,1,1,1,14,17],
     [5,7,7.5,9,14,17,18],
     [5,10,11,12,18,18,20],
     [5,15,16,16,20,23,27],
     [7,15,19,21,22,24,31],
     [12,16,22,22,24,25,34],
     [16,21,23,26,26,30,37]]
print s.kthSmallest2(a,49)
        