# https://leetcode.cn/problems/find-pivot-index

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums) + 1
        preSum = [0 for _ in range(n)]

        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        for i in range(1, n - 1):
            leftSum = preSum[i - 1] - preSum[0]
            rightSum = preSum[n - 1] - preSum[i]
            if leftSum == rightSum:
                return i - 1
            
        return -1
        

print(Solution().pivotIndex([2, 1, -1]))
