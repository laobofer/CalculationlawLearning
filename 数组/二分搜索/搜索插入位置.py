# https://leetcode.cn/problems/search-insert-position

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1

        return left