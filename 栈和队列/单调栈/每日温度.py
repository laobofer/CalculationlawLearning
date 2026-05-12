# https://leetcode.cn/problems/daily-temperatures

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0 for _ in range(n)]
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            res[i] = 0 if not stack else stack[-1][1] - i
            stack.append([temperatures[i], i])

        return res