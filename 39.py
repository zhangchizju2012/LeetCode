#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 23:28:38 2016

@author: zhangchi
"""

class Solution(object):
    '''
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            return ['a']
        elif target < min(candidates):
            return []
        else:
            final = []
            for item in candidates:
                #result = [item]
                for temp_result in self.combinationSum(candidates, target-item):
                    if temp_result == 'a':
                        final.append([item])
                    else:
                        #result = [item] + temp_result
                        final.append([item] + temp_result)
            return final
    '''
    '''
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        candidates.sort()
        if target == 0:
            return ['a']
        elif target < candidates[0]:
            return []
        else:
            final = []
            for item in candidates:
                #result = [item]
                for temp_result in self.combinationSum(candidates, target-item):
                    if temp_result == 'a':
                        if [item] not in final:
                            final.append([item])
                    else:
                        #result = [item] + temp_result
                        temp = sorted([item] + temp_result)
                        if temp not in final:
                            final.append([item] + temp_result)
            return final
    '''
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = list(set(candidates))
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret

    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)#等价于Solution.ret.append(valuelist)再return
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])#此处的start不是i+1，所以是可以用重复元素的，前面的元素不再扫描是因为其他情况会扫描到，就不重复了
            #print 1
S = Solution()
candidates = [6,7,8,9,10,2,3,4,5]
target = 10
print S.combinationSum(candidates, target)
        