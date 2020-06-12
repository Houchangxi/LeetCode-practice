#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 12:07:42 2020

@author: andrew
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
#         2种情况
        # 第一种情况：第一个房子不偷 后边的所有房子都可偷或不偷
        # 第二种情况：最后一个房子不偷 前边的所有房子都可偷或不偷
        # 这两种情况可以避免 arranged in a circle 的情况
        # 缺点是：会出现一点重复计算
        n = len(nums)
        if n==0:return 0
        if n==1:return nums[0]
        
        # 第一情况：第一个房子不偷 所以初始化的时候 rob的房子 从nums[1]开始 而循环计算从第三个开始
        rob = nums[1] 
        norob = 0
        for i in range(2,len(nums)):
            temp_rob = rob
            temp_norob = norob
            rob = temp_norob + nums[i]  #如果rob 上一次取norob的数+这次nums[i]
            norob = max(temp_rob, temp_norob) #如果norob 那么取上次rob和norob的最大值
        result = max(rob,norob)
        
        # 第二种情况：最后一个房子不偷 所有初始化的时候 从nums[0]开始 循环计算从第二个开始，结束循环倒数第二位
        rob = nums[0]
        norob = 0
        for i in range(1,len(nums)-1):
            temp_rob = rob
            temp_norob = norob
            rob = temp_norob + nums[i]  #如果rob 上一次取norob的数+这次nums[i]
            norob = max(temp_rob, temp_norob) #如果norob 那么取上次rob和norob的最大值
        result = max(result,rob,norob)
        return result
        
        