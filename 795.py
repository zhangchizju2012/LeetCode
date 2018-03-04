#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 20:02:08 2018

@author: zhangchi
"""

class Solution(object):
    # 碰到s了，就相当于从头开始了
    # 碰到o时，取决于之前有没有碰到过n, 没碰到，不会增加结果，
    # 碰到过，结果加的个数取决于之前最后一次碰到n时增加的个数（previous）
    # 扫到每一个，增加的个数代表，以当前这个为结尾的可能的个数
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """   
        result = 0
        count = 0
        label = False
        previous = 0
        for item in A:
            if L <= item <= R: # n (need) -> 至少得有一个
                label = True
                count += 1
                result += count
                previous = count

            elif item > R: # s (stop) -> 不能有
                label = False
                count = 0
            else: # o -> 有没有都没事
                if label is False:
                    count += 1
                else:
                    result += previous
                    count += 1
                        
        return result
    
s = Solution()
#print(s.numSubarrayBoundedMax([2, 1, 4, 3],2,2))
print(s.numSubarrayBoundedMax([73,55,36,5,55,14,9,7,72,52],32,69))
    
# =============================================================================
# [73,55,36,5,55,14,9,7,72,52]
# 32
# 69  
# expected = 22
# =============================================================================
# =============================================================================
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat Mar  3 20:02:08 2018
# 
# @author: zhangchi
# """
# 
# class Solution(object):
#     def numSubarrayBoundedMax(self, A, L, R):
#         """
#         :type A: List[int]
#         :type L: int
#         :type R: int
#         :rtype: int
#         """
# # =============================================================================
# #         need = [] # at least one
# #         stop = []
# #         
# #         for index, item in enumerate(A):
# #             if L <= item <= R:
# #                 need.append(index)
# #             elif item > R:
# #                 stop.append(index)
# # =============================================================================
#         
#         temp = []
#         
#         for index, item in enumerate(A):
#             if L <= item <= R:
#                 if len(temp) == 0:
#                     temp.append(["n",1])
#                 else:
#                     if temp[-1][0] == "n":
#                         temp[-1][1] += 1
#                     else:
#                         temp.append(["n",1])
# 
#             elif item > R:
#                 if len(temp) == 0:
#                     temp.append(["s",1])
#                 else:
#                     if temp[-1][0] == "s":
#                         temp[-1][1] += 1
#                     else:
#                         temp.append(["s",1])
#             else:
#                 if len(temp) == 0:
#                     temp.append(["o",1])
#                 else:
#                     if temp[-1][0] == "o":
#                         temp[-1][1] += 1
#                     else:
#                         temp.append(["o",1])
#                         
#         result = 0
#         count = 0
#         label = False
#         for item in temp:
#             if item[0] == "o" and label is False:
#                 count += item[1]
#             elif item[0] == "o" and label is True:
#                 
#             elif item[1] == "n":
#                 label = True
#                 count += 1
#                 result += count
#                 
# =============================================================================
