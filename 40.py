#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:49:15 2016

@author: zhangchi
"""

#或许可以联系第30题我自己的解法

class Solution(object):
    '''
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if target == 0:
            return ['a']
        elif len(candidates)==0 or target < min(candidates):
            return []
        else:
            final = []
            index = 0
            for item in candidates:
                #result = [item]
                #temp_candidates = [candidate for candidate in candidates if candidate!= item]
                temp_candidates = [candidates[i] for i in range(len(candidates)) if i != index]
                index = index + 1
                for temp_result in self.combinationSum2(temp_candidates, target-item):
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
    '''
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        if len(candidates)==0 or target < min(candidates):
            return []
        else:
            final = []
            index = 0
            for item in candidates:
                #result = [item]
                #temp_candidates = [candidate for candidate in candidates if candidate!= item]
                if target - item == 0:
                    if [item] not in final:
                        final.append([item])
                        break
                temp_candidates = [candidates[i] for i in range(len(candidates)) if i != index]
                index = index + 1
                for temp_result in self.combinationSum2(temp_candidates, target-item):
                        #result = [item] + temp_result
                    temp = sorted([item] + temp_result)
                    if temp not in final:
                        final.append([item] + temp_result)
            return final
    '''
    def combinationSum2(self, candidates, target): 
        # write your code here
        candidates.sort()        
        self.ans, tmp, use = [], [], [0] * len(candidates)        
        self.dfs(candidates, target, 0, 0, tmp, use)        
        return self.ans    
    def dfs(self, can, target, p, now, tmp, use):        
        if now == target:            
            self.ans.append(tmp[:])            
            return        
        for i in range(p, len(can)):#range(p, len(can))为了提高效率，避免重复运算，一个一个向前推进(特别是86行这里的i+1)，从而体现没有用重复的元素，跟use没什么关系，use只是用来区分相同的元素的取用情况，见之后那个comment            
            if now + can[i] <= target and (i == 0 or can[i] != can[i-1] or use[i-1] == 1):
                #这个和前一个相等，前一个又没用，就没必要尝试这个了#处理不重复元素三步骤，排序，range,向前推进，明天看看之前写的另一例子，看看能不能提高效率
                tmp.append(can[i])
                use[i] = 1                
                self.dfs(can, target, i+1, now + can[i], tmp, use)                
                tmp.pop()                
                use[i] = 0
S = Solution()
#candidates = [29,19,14,33,11,5,9,23,23,33,12,9,25,25,12,21,14,11,20,30,17,19,5,6,6,5,5,11,12,25,31,28,31,33,27,7,33,31,17,13,21,24,17,12,6,16,20,16,22,5]
candidates = [6,7,8,9,10,2,3,4,5]
target = 10
print S.combinationSum2(candidates, target)