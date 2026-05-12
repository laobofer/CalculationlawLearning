# https://leetcode.cn/problems/split-array-largest-sum

from typing import List

class Solution:
    def get_needed_k(self, nums, max_):
        temp = 0
        res = 0

        for num in nums:
            temp += num
            if temp > max_:
                temp = num
                res += 1
            elif temp == max_:
                temp = 0
                res += 1

        if temp != 0:
            res += 1

        return res

    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        if left == right:
            return left

        while left <= right:
            mid = left + (right - left) // 2
            needed_k = self.get_needed_k(nums, mid)

            if needed_k > k:
                left = mid + 1
            elif needed_k == k:
                right = mid - 1
            elif needed_k < k:
                right = mid - 1

        return left