# https://leetcode.cn/problems/search-in-rotated-sorted-array

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import bisect

        left, right = 0, len(nums) - 1
        index = 0

        while left <= right:
            mid = left + (right - left) // 2

            if left == right:
                break

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1

        res = 0
        index = left

        if target > nums[-1]:
            res = bisect.bisect_left(nums, target, 0, index)
        else:
            res = bisect.bisect_left(nums, target, index)

        return res if nums[res] == target else -1


print(Solution().search([3, 4, 5, 6, 1, 2], 2))