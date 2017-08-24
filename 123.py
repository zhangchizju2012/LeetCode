#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Reviewed on Wed Aug 23 21:43:41 2017

@author: zhangchi
"""

"""
Created on Mon Jun 12 18:43:49 2017

@author: zhangchi
"""

class Solution(object):
    # 这个解释最好理解（其实可以认为一天内可以完成两次交易）：
    # https://discuss.leetcode.com/topic/39751/my-explanation-for-o-n-solution
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1 = -float('inf')
        hold2 = -float('inf')
        release1 = 0
        release2 = 0
        for i in prices: # Assume we only have 0 money at first
            # hold1表示迄今为止最后一个有效动作是买第一个股票（之后可能rest，rest不算有效动作，只有买卖算有效），其他同理
            hold1    = max(hold1,    -i)#          // The maximum if we've just buy  1st stock so far. 
            release1 = max(release1, hold1+i)#     // The maximum if we've just sold 1nd stock so far.
            hold2    = max(hold2,    release1-i)#  // The maximum if we've just buy  2nd stock so far.
            release2 = max(release2, hold2+i)#     // The maximum if we've just sold 2nd stock so far.
            # 上下两种都是可以的，上面做法的理解方式：一个时间点，就可以把所有的买卖流程完成（可以进行两次买卖）
            # 下面做法的理解方式：一个时间点就做一个操作，要么买，要么卖，要么休息，后面的状态和之前的状态有关
            # 所以更新状态的时候要先更新后面的，否则会被干扰
            # 之所以两者等价，是因为，最优的做法，一个时间点肯定就是做一个操作，但是一个时间点完成完成所有事，已经包含了这种
            # 一个时间点肯定就是做一个操作的最优情况，且其他可能的情况都不会优于一个时间点做一个操作的情况
# =============================================================================
#             release2 = max(release2, hold2+i)#     // The maximum if we've just sold 2nd stock so far.
#             hold2    = max(hold2,    release1-i)#  // The maximum if we've just buy  2nd stock so far.
#             release1 = max(release1, hold1+i)#     // The maximum if we've just sold 1nd stock so far.
#             hold1    = max(hold1,    -i)#          // The maximum if we've just buy  1st stock so far. 
# =============================================================================
        return release2 # Since release1 is initiated as 0, so release2 will always higher than release1.
    
s = Solution()
print s.maxProfit([1,3])