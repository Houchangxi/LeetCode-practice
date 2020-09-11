#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:04:42 2020

@author: andrew
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result