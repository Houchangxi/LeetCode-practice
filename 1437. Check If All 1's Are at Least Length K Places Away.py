#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:26:28 2020

@author: HouChangxi
"""

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        fast =2
        slow =0
        l = len(nums)
        while fast < l:
            if nums[fast]==1:
                if fast - slow <k+1:
                    return False
                slow=fast
            fast +=1
        return 
    
# 此题用快慢指针即可解决，问题点在于考虑边界条件，fast的指针初始值为2 慢指针为0  还有就是k是指2个1之间的距离而不是简单的index之差 所以要k+1 
# 我们只需要找到最近的2个1之间的距离是否满足条件即可 如果最近的2个1都满足条件 即都满足条件