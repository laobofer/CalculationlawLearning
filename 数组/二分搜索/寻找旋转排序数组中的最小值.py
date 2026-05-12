# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if left == right:
                break

            if nums[mid] <= nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]
    
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
        