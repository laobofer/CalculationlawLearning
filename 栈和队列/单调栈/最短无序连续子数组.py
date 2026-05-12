# https://leetcode.cn/problems/shortest-unsorted-continuous-subarray

from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        res = []

        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                res.append(i)

        if len(res) >= 2:
            res = res[-1] - res[0] + 1
        elif len(res) == 1:
            res = len(nums) - res[0]
        else:
            res = 0

        return res
