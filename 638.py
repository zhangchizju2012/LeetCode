#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 20:12:50 2017

@author: zhangchi
"""

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        if price == len(price) * [0]:
            return 0
        self.dic = {}
        self.length = len(price)
        for item in special:
            if tuple(item[:-1]) in self.dic:
                self.dic[tuple(item[:-1])] = min(self.dic[tuple(item[:-1])],item[-1])        
            else:
                self.dic[tuple(item[:-1])] = item[-1]
        self.prices = price
        # 单个单个的不要当成special, 若当成special的话会很慢，通过61行那里来处理单个的问题
        # 比赛的时候就是因为这个导致速度一直无法提升
#==============================================================================
#         for i in xrange(self.length):
#             self.dic[tuple(i*[0]+[1]+(self.length-i-1)*[0])] = price[i]
#==============================================================================
        self.choices = self.dic.keys()
        self.choicesLength = len(self.choices)
        self.mem = dict(self.dic)
        return self.helper(needs,0)
        
    def helper(self, needs, index):
        # dfs, index用来避免重复地扫描，前面扫过的就不扫了
        if tuple(needs) not in self.mem:
            if needs == [0] * self.length:
                self.mem[tuple(needs)] = 0
            else:
                minValue = float('inf')
                for j in xrange(index,self.choicesLength):
                    choice = self.choices[j]
                    if self.dic[choice] < minValue:
                #for choice in self.dic:
                        changeNeed = []
                        label = True
                        for i in xrange(self.length):
                            if needs[i] >= choice[i]:
                                changeNeed.append(needs[i]-choice[i])
                            else: # 说明用special会超过需求量，所以不能采用special
                                label = False
                                break
                        if label:
                            temp = self.helper(changeNeed,j)+self.dic[choice]
                            minValue = min(minValue, temp)
                another = 0
                # 不用special package来解决，单个单个来解决
                for i in xrange(self.length):
                    if needs[i] != 0:
                        another += needs[i] * self.prices[i]
                minValue = min(minValue, another)
                self.mem[tuple(needs)] = minValue
        return self.mem[tuple(needs)]
        
s = Solution()
print s.shoppingOffers([9,6,1,5,3,4],[[1,2,2,1,0,4,14],[6,3,4,0,0,1,16],[4,5,6,6,2,4,26],[1,1,4,3,4,3,15],[4,2,5,4,4,5,15],[4,0,0,2,3,5,13],[2,4,6,4,3,5,7],[3,3,4,2,2,6,21],[0,3,0,2,3,3,15],[0,2,4,2,2,5,24],[4,1,5,4,5,4,25],[6,0,5,0,1,1,14],[4,0,5,2,1,5,8],[4,1,4,4,3,1,10],[4,4,2,1,5,0,14],[2,4,4,1,3,1,16],[4,2,3,1,2,1,26],[2,4,1,6,5,3,2],[0,2,0,4,0,0,19],[3,1,6,3,3,1,23],[6,2,3,2,4,4,16],[5,3,5,5,0,4,5],[5,0,4,3,0,2,20],[5,3,1,2,2,5,8],[3,0,6,1,0,2,10],[5,6,6,1,0,4,12],[0,6,6,4,6,4,21],[0,4,6,5,0,0,22],[0,4,2,4,4,6,16],[4,2,1,0,6,5,14],[0,1,3,5,0,3,8],[5,5,3,3,2,0,4],[1,0,3,6,2,3,18],[4,2,6,2,2,5,2],[0,2,5,5,3,6,12],[1,0,6,6,5,0,10],[6,0,0,5,5,1,24],[1,4,6,5,6,3,19],[2,2,4,2,4,2,20],[5,6,1,4,0,5,3],[3,3,2,2,1,0,14],[0,1,3,6,5,0,9],[5,3,6,5,3,3,11],[5,3,3,1,0,2,26],[0,1,1,4,2,1,16],[4,2,3,2,1,4,6],[0,2,1,3,3,5,15],[5,6,4,1,2,5,18],[1,0,0,1,6,1,16],[2,0,6,6,2,2,17],[4,4,0,2,4,6,12],[0,5,2,5,4,6,6],[5,2,1,6,2,1,24],[2,0,2,2,0,1,14],[1,1,0,5,3,5,16],[0,2,3,5,5,5,6],[3,2,0,6,4,6,8],[4,0,1,4,5,1,6],[5,0,5,6,6,3,7],[2,6,0,0,2,1,25],[0,4,6,1,4,4,6],[6,3,1,4,1,1,24],[6,2,1,2,1,4,4],[0,1,2,3,0,1,3],[0,2,5,6,5,2,13],[2,6,4,2,2,3,17],[3,4,5,0,5,4,20],[6,2,3,4,1,3,4],[6,4,0,0,0,5,16],[3,1,2,5,0,6,11],[1,3,2,2,5,6,14],[1,3,4,5,3,5,18],[2,1,1,2,6,1,1],[4,0,4,0,6,6,8],[4,6,0,5,0,2,1],[3,1,0,5,3,2,26],[4,0,4,0,6,6,6],[5,0,0,0,0,4,26],[4,3,2,2,0,2,14],[5,2,4,0,2,2,26],[3,4,6,0,2,4,25],[2,1,5,5,1,3,26],[0,5,2,4,0,2,24],[5,2,5,4,5,0,1],[5,3,0,1,5,4,15],[6,1,5,1,2,1,21],[2,5,1,2,1,4,15],[1,4,4,0,0,0,1],[5,0,6,1,1,4,22],[0,1,1,6,1,4,1],[1,6,0,3,2,2,17],[3,4,3,3,1,5,17],[1,5,5,4,5,2,27],[0,6,5,5,0,0,26],[1,4,0,3,1,0,13],[1,0,3,5,2,4,5],[2,2,2,3,0,0,11],[3,2,2,1,1,1,6],[6,6,1,1,1,6,26],[1,5,1,2,5,2,12]],[6,6,6,1,6,6])
#print s.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1])
#print s.shoppingOffers([9,9],[[1,1,1]],[9,9])