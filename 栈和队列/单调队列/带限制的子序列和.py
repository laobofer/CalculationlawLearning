# https://leetcode.cn/problems/constrained-subsequence-sum

from typing import List

class MonotonicQueue:
    def __init__(self):
        import collections

        self.q = collections.deque()
        self.maxq = collections.deque()
        self.minq = collections.deque()

    def push(self, elem: int):
        self.q.append(elem)

        while self.maxq and self.maxq[-1] < elem:
            self.maxq.pop()
        self.maxq.append(elem)

        while self.minq and self.minq[-1] > elem:
            self.minq.pop()
        self.minq.append(elem)

    def max(self) -> int:
        return self.maxq[0]

    def min(self) -> int:
        return self.minq[0]

    def pop(self):
        deleteVal = self.q.popleft()

        if deleteVal == self.maxq[0]:
            self.maxq.popleft()
        if deleteVal == self.minq[0]:
            self.minq.popleft()

    def size(self) -> int:
        return len(self.q)

    def isEmpty(self) -> bool:
        return not self.q


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [nums[0] for _ in range(n)]
        window = MonotonicQueue()
        window.push(dp[0])

        for i in range(1, n):
            dp[i] = max(nums[i], window.max() + nums[i])

            while window.size() >= k:
                window.pop()

            window.push(dp[i])

        return max(dp)