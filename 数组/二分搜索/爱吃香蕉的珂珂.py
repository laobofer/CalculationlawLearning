# https://leetcode.cn/problems/koko-eating-bananas

from typing import List

class Solution:
    def get_time_required(self, piles, v):
        res = 0
        for pile in piles:
            res += pile // v
            if pile % v != 0:
                res += 1

        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 1000000000

        while left <= right:
            mid = left + (right - left) // 2
            needed_time = self.get_time_required(piles, mid)
            if needed_time == h:
                right = mid - 1
            elif needed_time < h:
                right = mid - 1
            elif needed_time > h:
                left = mid + 1

        return left