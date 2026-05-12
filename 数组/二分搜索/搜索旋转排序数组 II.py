# https://leetcode.cn/problems/search-in-rotated-sorted-array-ii

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            while left + 1 < len(nums) and nums[left] == nums[left + 1]:
                left += 1
            while right - 1 >= 0 and nums[right] == nums[right - 1]:
                right -= 1

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
