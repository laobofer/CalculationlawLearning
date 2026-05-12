# https://leetcode.cn/problems/search-a-2d-matrix-ii

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            num = matrix[i][j]
            if num == target:
                return True
            elif num > target:
                j -= 1
            elif num < target:
                i += 1

        return False