# https://leetcode.cn/problems/maximum-sum-circular-subarray

from typing import List

class MonotonicQueue:
    def __init__(self):
        from collections import deque
        self.minq = deque()

    def min(self):
        return self.minq[0]

    def push(self, val):
        while self.minq and val < self.minq[-1]:
            self.minq.pop()

        self.minq.append(val)

    def pop(self, val):
        if self.minq and self.minq[0] == val:
            self.minq.popleft()


class Solution:
    def need_shrink(self, left: int, right: int, limit: int) -> bool:
        """当窗口内前缀和的索引跨度超过 limit 时，需要收缩左边界"""
        return right - left > limit + 1

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        L = len(nums)
        nums_ext = nums + nums
        n = 2 * L + 1
        preSum = [0] * n
        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums_ext[i - 1]

        res = -float("inf")
        window = MonotonicQueue()
        left, right = 0, 0

        while right < n:
            num = preSum[right]
            right += 1
            window.push(num)
            

            while self.need_shrink(left, right, L):
                num_ = preSum[left]
                window.pop(num_)
                left += 1

            res = max(res, num - window.min())

        return res if res != 0 else max(nums)