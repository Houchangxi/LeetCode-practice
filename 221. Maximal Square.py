#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:28:40 2020

@author: andrew
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        max_line = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        max_line = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == str(1):
                    dp[i+1][j+1] = min(dp[i][j+1],dp[i][j],dp[i+1][j]) +1
                max_line = max(max_line,dp[i+1][j+1])
        print(dp)
        return max_line*max_line
#     此题需要多加一行一列 为零的数据 避免[["1"]]的特殊情况 对照题目参见1277