#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:41:17 2020

@author: andrew
"""

#       卷积解法：
#       1、卷积当中两个矩阵的 dot乘 即为两个矩阵中 格子中数字为1的 重叠数量之和  （这个概念至关重要）
#       2、根据卷积概念 B添加padding 为2 并且strip 为1  在3*3的矩阵数组中 padding为2 可以得到如下图的矩阵
         #[[0000000]
         # [0000000]
         # [0000000]
         # [0010100]
         # [0010000]
         # [0000000]
         # [0000000]]
#       3、A矩阵从左上角开始strip 遍历整个B数组padding之后 重复最大的值 即为答案
        import numpy as np
        A = np.array(A)
        B = np.array(B)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps  