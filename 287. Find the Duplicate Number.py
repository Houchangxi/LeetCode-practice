#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:16:22 2020

@author: andrew
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # dic = collections.Counter(nums)
        # for key,val in dic.items():
        #     if val >=2 :
        #         return key
        
        
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
    
#     快慢指针 可参见https://leetcode-cn.com/problems/find-the-duplicate-number/