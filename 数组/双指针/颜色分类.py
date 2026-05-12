# https://leetcode.cn/problems/sort-colors

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = max(nums) + 1
        count = [0 for _ in range(len_)]

        for num in nums:
            count[num] += 1
        
        i = -1
        for index in count:
            for _ in range(index):
                i += 1
                nums[i] = index


