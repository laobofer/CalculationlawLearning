# https://leetcode.cn/problems/largest-rectangle-in-histogram

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        stack2 = []

        right = [0 for _ in range(n)]
        left = [0 for _ in range(n)]

        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()

            right[i] = n if not stack else stack[-1][1]
            stack.append([heights[i], i])

        for i in range(0, n):
            while stack2 and stack2[-1][0] >= heights[i]:
                stack2.pop()

            left[i] = -1 if not stack2 else stack2[-1][1]
            stack2.append([heights[i], i])

        areas = [(right[i] - left[i] - 1) * heights[i] for i in range(n)]
        return max(areas)
    

print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))