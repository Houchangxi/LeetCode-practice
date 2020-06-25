#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:17:59 2020

@author: andrew
"""

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        all = self.countNodes(root.left)  + self.countNodes(root.right) +1
        return all