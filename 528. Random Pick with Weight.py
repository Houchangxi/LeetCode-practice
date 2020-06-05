#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:21:46 2020

@author: andrew
"""

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        for i in range(1,self.n):
            w[i] += w[i-1]
        self.s = self.w[-1]
     

    def pickIndex(self) -> int:

        seed = random.randint(1,self.s)
        l,r = 0, self.n-1
        while l<r:
            mid = (l+r)//2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l
        
# 此题关键是要理解题意，我也是看了好几遍，[1,4,6,9,5] 这个数组index的[0,1,2,3,4]的获取概率为 [1,5,11,20,25] 即每一位的数是前一位的累加和  比如 index = 4 的获得概率 应该是随机数[1,25]之间 落在20-25的概率  然后随机一个seed 这个seed用二分法查找 落在那个区间了 把left的index 输出即可  

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
        
    