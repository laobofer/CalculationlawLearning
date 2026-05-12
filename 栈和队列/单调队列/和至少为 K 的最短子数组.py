# https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k

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
    def need_shrink(self, window, k, right, preSum):
        if right >= len(preSum):
            return False

        return preSum[right] - window.min() >= k

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums) + 1
        preSum = [0 for _ in range(n)]
        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        left, right = 0, 0
        window = MonotonicQueue()
        res = 1000000

        while right < n:
            num = preSum[right]
            right += 1
            window.push(num)

            while left < right and self.need_shrink(window, k, right, preSum):
                res = min(res, right - left)

                num = preSum[left]
                left += 1
                window.pop(num)

        return res if res < 1000000 else -1

