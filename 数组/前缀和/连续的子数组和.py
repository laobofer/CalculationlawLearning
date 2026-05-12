# https://leetcode.cn/problems/continuous-subarray-sum

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums) + 1
        preSum = [0 for _ in range(n)]

        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        dict = {}
        # 前缀和到索引的映射
        for i in range(n):
            if preSum[i] % k not in dict:
                dict[preSum[i] % k] = i

        for i in range(1, n):
            need = preSum[i] % k
            if need in dict and i - dict[need] >= 2:
                return True

        return False

print(Solution().checkSubarraySum([23, 2, 4, 6, 6], 7))            
