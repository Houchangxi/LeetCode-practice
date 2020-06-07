#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:15:46 2020

@author: andrew
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for c in range(1, amount + 1):
            dp[0][c] = 0  # 没有任何一种硬币，不论需要多少金额，都没有对应的方案数
        for r in range(len(coins) + 1):
            dp[r][0] = 1  # 如果金额为0，对多少种硬币来说都是1种方案
        
        for i in range(1,n+1):
            for j in range(amount+1):
                # 第一种方式 dp[i][j] = sum(dp[i-1][j-k*coins[i-1]]), 0<=k<=j/coins[i-1]  O(n*m^2)
                # for k in range(j//coins[i-1]+1):
                #     dp[i][j] += dp[i-1][j-k*coins[i-1]]
                # 从上边的方案进行优化  不再做k循环 因为直接从公式可得 dp[i][j-coins[i-1]]
                dp[i][j] = dp[i-1][j] + (dp[i][j-coins[i-1]] if coins[i-1] <=j else 0)
                
                # 再进一步优化空间  g[j] = g[j] + g[j-coins[i-1]]
                # 详细解题可参考：https://www.youtube.com/watch?v=ZKAILBWl08g
        return dp[-1][-1]