# https://leetcode.cn/problems/shift-2d-grid

# 想要交换数组的某两部分 0 - k, k + 1 到 n - 1, 可以用三次反转的方法 

from typing import List

class Solution:
    def grid_move(self, grid):
        lst = [e.pop() for e in grid]
        v = lst.pop()
        lst.insert(0, v)
        for row in grid:
            row.insert(0, lst.pop(0))


    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k):
            self.grid_move(grid)

        return grid
    
class s:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        k = k % (m * n)

        self.reverse(grid, 0, m * n - k - 1)
        self.reverse(grid, m * n - k, m * n - 1)
        self.reverse(grid, 0, m * n - 1)

        return grid


    def get(self, grid, index):
        i = index // len(grid[0])
        j = index % len(grid[0])
        return grid[i][j]

    def set(self, grid, index, val):
        i = index // len(grid[0])
        j = index % len(grid[0])
        grid[i][j] = val

    def reverse(self, grid, i, j):
        while i < j:
            val_1 = self.get(grid, i)
            val_2 = self.get(grid, j)

            self.set(grid, i, val_2)
            self.set(grid, j, val_1)

            i += 1
            j -= 1

    