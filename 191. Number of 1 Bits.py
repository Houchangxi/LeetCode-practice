#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:10:26 2020

@author: andrew
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ans = 0
        while(n!=0):
            n &= (n-1)
            ans += 1
        return ans
    
#     此题为技巧题 题意是一个无符号的int 变成二进制 有多少个1
#     &与的关系 特点   如果n和n-1连个数进行 &预算 
#     如：  1010和 1001  &后  = 1000  即10和01 & 变为00
#     n 的每一次 &= 都会消除掉最末尾的1  所以消除几次变为0 就有几个1