# https://leetcode.cn/problems/sort-the-matrix-diagonally

from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dict = {}
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if (i - j) not in dict:
                    dict[i - j] = []
                dict[i - j].append(mat[i][j])

        for i in dict.values():
            i.sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = dict[i - j].pop()

        return mat



s = Solution()
print(s.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
        