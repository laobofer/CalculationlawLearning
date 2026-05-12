# https://leetcode.cn/problems/find-peak-element

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if left == right:
                return left

            if nums[mid] > nums[mid + 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
        return left

print(Solution().findPeakElement([1, 2, 3, 1]))