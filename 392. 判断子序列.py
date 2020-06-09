#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:57:22 2020

@author: andrew
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 快慢指针
        # fast,slow = 0,0
        # if len(s)<1:
        #     return True
        # while fast < len(t):
        #     if t[fast]==s[slow]:
        #         fast +=1
        #         slow +=1
        #         if slow==len(s):
        #             return True
        #     else:
        #         fast +=1
        # return False
    
        # dp解决
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        print(dp)
        
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+ 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        print(dp)
        return True if dp[-1][-1] == len(s) else False