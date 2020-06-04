#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:18:29 2020

@author: andrew
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
#         DP解法
        if len(costs)==0:
            return 0
        n = len(costs)
        m = len(costs[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            dp[n-1][i] = costs[n-1][i]
        for j in range(n-2,-1,-1):
            dp[j][0] = costs[j][0]+min(dp[j+1][1],dp[j+1][2])
            dp[j][1] = costs[j][1]+min(dp[j+1][0],dp[j+1][2])
            dp[j][2] = costs[j][2]+min(dp[j+1][1],dp[j+1][0])
        return min(dp[0])
        
#         递归解法 没有 memo 超时 加memo可过
#         if len(costs)==0:
#             return 0
#         return min(self.helper(0,0,len(costs)-1,costs),self.helper(0,1,len(costs)-1,costs),self.helper(0,2,len(costs)-1,costs))
        
#     def helper(self,n,color,limit,costs):
#         total_cost = costs[n][color]
#         if n==limit:
#             pass
#         elif color==0:
#             total_cost += min(self.helper(n+1,1,limit,costs),self.helper(n+1,2,limit,costs))
#         elif color==1:
#             total_cost += min(self.helper(n+1,0,limit,costs),self.helper(n+1,2,limit,costs))
#         elif color==2:
#             total_cost += min(self.helper(n+1,0,limit,costs),self.helper(n+1,1,limit,costs))
#         return total_cost