# https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = [0 for _ in range(n)]
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            discount = 0 if not stack else stack[-1]
            res[i] = prices[i] - discount
            stack.append(prices[i])

        return res