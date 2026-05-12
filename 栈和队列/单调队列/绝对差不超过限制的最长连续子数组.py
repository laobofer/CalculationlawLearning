# https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit

from typing import List

class MonotonicQueue:
    def __init__(self):
        from collections import deque

        self.maxq = deque()
        self.minq = deque()

    def max(self):
        return self.maxq[0]

    def min(self):
        return self.minq[0]

    def push(self, val):
        while self.maxq and val > self.maxq[-1]:
            self.maxq.pop()

        while self.minq and val < self.minq[-1]:
            self.minq.pop()

        self.maxq.append(val)
        self.minq.append(val)

    def pop(self, val):
        if val == self.maxq[0]:
            self.maxq.popleft()

        if val == self.minq[0]:
            self.minq.popleft()


class Solution:
    def need_shrink(self, window, limit):
        return abs(window.max() - window.min()) > limit

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right = 0, 0
        window = MonotonicQueue()
        res = 0

        while right < len(nums):
            num = nums[right]
            right += 1
            window.push(num)

            while left < right and self.need_shrink(window, limit):
                num = nums[left]
                left += 1
                window.pop(num)

            res = max(right - left, res)

        return res
