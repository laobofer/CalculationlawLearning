# https://leetcode.cn/problems/range-sum-query-2d-immutable

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        self.preSum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                self.preSum[i][j] = self.preSum[i - 1][j] + self.preSum[i][j - 1] - self.preSum[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.preSum[row2 + 1][col2 + 1]
            - self.preSum[row1][col2 + 1]
            - self.preSum[row2 + 1][col1]
            + self.preSum[row1][col1]
        ) 
