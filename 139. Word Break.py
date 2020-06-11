#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:57:54 2020

@author: andrew
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
        
#         此题可以用递归解决 可以看youtube 讲的很详细https://www.youtube.com/watch?v=ptlwluzeC1I