# https://leetcode.cn/problems/two-sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        temp = sorted(enumerate(nums), key=lambda x: x[1])

        while i < j:
            sum = temp[i][1] + temp[j][1]

            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [temp[i][0], temp[j][0]]
            
        return []