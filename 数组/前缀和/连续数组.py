# https://leetcode.cn/problems/contiguous-array

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums) + 1
        preSum = [0 for _ in range(n)]

        for i in range(1, n):
            preSum[i] = preSum[i - 1] + (-1 if nums[i - 1] == 0 else 1)

        dict = {}
        res = 0

        for i in range(n):
            if preSum[i] not in dict:
                dict[preSum[i]] = i
            else:
                res = max(res, i - dict[preSum[i]])
        
        return res
