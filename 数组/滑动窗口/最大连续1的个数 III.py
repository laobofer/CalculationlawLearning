# https://leetcode.cn/problems/max-consecutive-ones-iii

from typing import List

class Solution:
    def need_shrink(self, window, k):
        return window > k


    def longestOnes(self, nums: List[int], k: int) -> int:
        window = 0

        left, right = 0, 0
        res = 0

        while right < len(nums):
            num = nums[right]
            window += 0 if num == 1 else 1
            right += 1

            while left < right and self.need_shrink(window, k):
                num = nums[left]
                window -= 1 if num == 0 else 0
                left += 1

            res = max(res, right - left)

        return res

            
