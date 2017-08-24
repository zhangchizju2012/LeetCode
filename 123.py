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

# 后续问题：如果每次只能进行一个操作，且只能交易两次，不能多不能少，最大收益多少
# 用下面的，所有初始化为负无穷大，return release2，如果是负无穷，表示数据不够多（<4），其他情况都是对的

class Solution(object):
    # 这个解释最好理解（其实可以认为一天内可以完成两次交易）：
    # https://discuss.leetcode.com/topic/39751/my-explanation-for-o-n-solution
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 初始化（n=0）很重要，不同的问题不同的初始化，要点在于对于初始的几次(n=1)，要保证答案的正确性
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
            # 对于上面的，初始化可以把所有的都初始化为负无穷，因为他是认为一个时间点就可以把所有的买卖流程完成
            # 对于下面的，这样初始化是为了保证最大的肯定是release2，即使数据长度不够
            # 下面做法的理解方式：一个时间点就做一个操作，要么买，要么卖，要么休息，后面的状态和之前的状态有关
            # 所以更新状态的时候要先更新后面的，否则会被干扰 (一层一层传递的感觉)
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
print s.maxProfit([1,3,3,1])