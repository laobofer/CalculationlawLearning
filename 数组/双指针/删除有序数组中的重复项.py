# https://leetcode.cn/problems/remove-duplicates-from-sorted-array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        target = -101
        ret = 0

        while fast < len(nums):
            if target != nums[fast]:
                nums[slow] = nums[fast]
                target = nums[fast]
                slow += 1
                ret += 1

            fast += 1

        return ret



