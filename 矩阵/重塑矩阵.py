# https://leetcode.cn/problems/reshape-the-matrix

from typing import List

class Solution:
    def get(self, mat, index, col):
        i = index // col
        j = index % col

        return mat[i][j]
    
    def set(self, mat, index, col, val):
        i = index // col
        j = index % col

        mat[i][j] = val        

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        res = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(m * n):
            self.set(res, i, c, self.get(mat, i, n))

        return res