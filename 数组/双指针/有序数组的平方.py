# https://leetcode.cn/problems/squares-of-a-sorted-array

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        p = len(nums) - 1
        ret = [0 for _ in range(len(nums))]

        while i <= j:
            if nums[i] ** 2 >= nums[j] ** 2:
                ret[p] = nums[i] ** 2
                i += 1
            else:
                ret[p] = nums[j] ** 2
                j -= 1

            p -= 1

        return ret



        