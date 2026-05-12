# https://leetcode.cn/problems/minimum-size-subarray-sum

from typing import List

class Solution:
    def need_shrink(self, window, target):
        return window >= target
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        left , right = 0, 0
        res = 1e6

        while right < len(nums):
            num = nums[right]
            window += num
            right += 1

            while left < right and self.need_shrink(window, target):
                res = min(right - left, res)
                num = nums[left]
                window -= num
                left += 1

        return res if res != 1e6 else 0
