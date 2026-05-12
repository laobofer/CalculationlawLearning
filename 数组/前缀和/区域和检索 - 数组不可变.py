# https://leetcode.cn/problems/range-sum-query-immutable

from typing import List

# 可以快速计算区间里元素的和(或其他可逆的运算)

class NumArray:
    def __init__(self, nums: List[int]):
        self.preSum = [0 for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            self.preSum[i] = self.preSum[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
