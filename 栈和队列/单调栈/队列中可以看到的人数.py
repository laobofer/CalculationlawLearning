# https://leetcode.cn/problems/number-of-visible-people-in-a-queue

from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0 for _ in range(n)]
        stack = []

        for i in range(n - 1, -1, -1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1

            res[i] = count if not stack else count + 1
            stack.append(heights[i])

        return res
    

print(Solution().canSeePersonsCount([10, 6, 8, 5, 11, 9]))