# https://leetcode.cn/problems/matrix-block-sum

from typing import List

class Solution:
    def get_preSum(self, matrix: List[List[int]]):
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        preSum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1] + matrix[i - 1][j - 1]

        return preSum

    def sumRegion(self, preSum, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            preSum[row2 + 1][col2 + 1]
            - preSum[row1][col2 + 1]
            - preSum[row2 + 1][col1]
            + preSum[row1][col1]
        ) 
    
    def getSum(self, preSum, row1, col1, row2, col2, max_row, max_col):
        row2 = min(row2, max_row)
        col2 = min(col2, max_col)
        row1 = max(row1, 0)
        col1 = max(col1, 0)

        return self.sumRegion(preSum, row1, col1, row2, col2)


    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        preSum = self.get_preSum(mat)
        m, n = len(mat), len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]


        for i in range(m):
            for j in range(n):
                res[i][j] = self.getSum(preSum, i - k, j - k, i + k, j + k, m - 1, n - 1)

        return res
    

print(Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))