#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:37:04 2020

@author: andrew
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)]  for _ in  range(m)]
        ans =0
        for i in range(n):
            if matrix[0][i]==1:
                dp[0][i] =1
                
        for j in range(m):
            if matrix[j][0] ==1:
                dp[j][0] =1
                
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] ==1:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) +1
        return sum(map(sum,dp))

    
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# 如上边的矩阵可以得到一个动态规划的 计算公式  当matrix[i][j]==1时  第dp[i][j]的含有的正方形是来自于dp[i-1][j],dp[i-1][j-1],dp[i][j-1] 三个格子最小的矩阵个数 再加上1（本身==1）。 而这种计算需要先把行列的边界首先进行处理 matrix[0][i]==1和 matrix[j][0] ==1 先进行填充 然后循环dp  最终结果是dp的所有行列的sum