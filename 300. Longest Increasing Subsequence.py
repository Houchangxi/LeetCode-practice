#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:09:37 2020

@author: andrew
"""

class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums)==0:
            return 0
      # 动态规划解决 新建一个len相同的数组 然后dp记录
        # 10
        # [1]
        # 10,9
        # [1,1]
        # 10,9,2
        # [1,1,1]
        # 10,9,2,5
        # [1,1,1,2]
        # 10,9,2,5,3
        # [1,1,1,2,2]
        # 10,9,2,5,3,7
        # [1,1,1,2,2,3]
        
        
        length = len(nums)
        dp = [1] * length
        for i in range(length):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)
    
if __name__ == "__main__":
    solution = Solution()
    nums = [10,9,2,5,3,7,101,18]
    ans =solution.lengthOfLIS(nums)
    print(ans)