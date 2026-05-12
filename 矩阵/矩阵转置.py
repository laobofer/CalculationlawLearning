# https://leetcode.cn/problems/transpose-matrix

from typing import List

# 这个没有什么更好的办法
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))