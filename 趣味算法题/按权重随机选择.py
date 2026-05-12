# https://leetcode.cn/problems/random-pick-with-weight

from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.n = len(w) + 1
        self.preSum = [0 for _ in range(self.n)]
        for i in range(1, self.n):
            self.preSum[i] = self.preSum[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        import bisect
        import random
        target = random.randint(1, self.preSum[-1])
        index = bisect.bisect_left(self.preSum, target) - 1
        return index