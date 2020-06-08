#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:41:04 2020

@author: andrew
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 位运算符法
        if n==0:
            return False
        return n&(n-1) ==0
        
        
        #       优化版本 二分法
        # if n==0:
        #     return False
        # while n%2==0:
        #     n/=2
        # return n==1
        
#       用二分法做的
#         if n==1:
#             return True
#         if n<=0:
#             return False
#         left, right = 1,n
        
#         while left < right:
#             if right % 2 != 0:
#                 return False
#             mid = (left+right)//2
#             if mid <=right:
#                 right = mid
#         return True

# 此题还有相类似的题 Power of Three 326  Power of Four  342 可以考虑一起做 都为easy练手题