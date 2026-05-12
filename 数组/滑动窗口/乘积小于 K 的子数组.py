# https://leetcode.cn/problems/subarray-product-less-than-k

from typing import List

class Solution:
    def need_shrink(self, window, k):
        return window >= k


    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window = 1

        left, right = 0, 0
        res = 0
        while right < len(nums):
            num = nums[right]
            window *= num
            right += 1

            while left < right and self.need_shrink(window, k):               
                num = nums[left]
                window = window // num
                left += 1

            res += right - left               

        return res

print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))