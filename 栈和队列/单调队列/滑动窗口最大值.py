# https://leetcode.cn/problems/sliding-window-maximum

from typing import List

# 维护队列元素「先进先出」的时间顺序，又能够正确维护队列中所有元素的最值

class MonotonicQueue:
    def __init__(self):
        from collections import deque
        self.q = deque()

    def max(self):
        return self.q[0]
    
    def push(self, val):
        while self.q and val > self.q[-1]:
            self.q.pop()

        self.q.append(val)

    def pop(self, val):
        if val == self.q[0]:
            self.q.popleft()

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        window = MonotonicQueue()
        res = []

        while right < len(nums):
            num = nums[right]
            right += 1
            window.push(num)

            while left < right and right - left > k:
                num = nums[left]
                left += 1
                window.pop(num)

            if right - left == k:
                print(right, left)
                res.append(window.max())

        return res


print(Solution().maxSlidingWindow([1, -1], 1))