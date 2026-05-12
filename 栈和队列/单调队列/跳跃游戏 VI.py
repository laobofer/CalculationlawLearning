# https://leetcode.cn/problems/jump-game-vi

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
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window = MonotonicQueue()        
        dp = [-float('inf') for _ in range(n)]

        window.push(nums[0])
        dp[0] = window.max()

        for i in range(1, n):
            dp[i] = window.max() + nums[i]

            while window.size() >= k:
                window.pop()

            window.push(dp[i])

        return dp[n - 1]
