# https://leetcode.cn/problems/search-a-2d-matrix

from typing import List

class Solution:
    def get(self, mat, index):
        col = len(mat[0])
        i, j = index // col, index % col

        return mat[i][j]


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_num = self.get(matrix, mid)

            if mid_num < target:
                left = mid + 1
            elif mid_num == target:
                return True
            elif mid_num > target:
                right = mid - 1

        return False
                