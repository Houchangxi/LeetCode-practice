#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:01:31 2020

@author: andrew
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        
        if n*m==0:
            return n+m
        
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in  range(n+1):
            dp[i][0]=i
        for j in range(m+1):
            dp[0][j]=j
        
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                c = 1 if word1[i-1] != word2[j-1] else 0
                dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+c)
        return dp[n][m]
    
    # 此题经典 dp 题 直接去看vedio解释 https://www.youtube.com/watch?v=Q4i_rqON2-E