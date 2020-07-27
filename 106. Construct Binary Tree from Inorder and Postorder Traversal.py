#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:44:06 2020

@author: andrew
"""

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#       终止条件
        if not inorder or not postorder:
            return None

        rootval = postorder[-1]
        root = TreeNode(rootval)
        inorderIndex = inorder.index(rootval)
#       参考105题 通过inorder 来判断左子树和右子树  postorder 寻找根结点  pre和post的根结点遍历方式正好相反
        root.left = self.buildTree(inorder[:inorderIndex],postorder[:inorderIndex])
        root.right =self.buildTree(inorder[inorderIndex+1:],postorder[inorderIndex:-1])
        
        return root