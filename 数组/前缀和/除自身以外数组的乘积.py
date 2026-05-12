# https://leetcode.cn/problems/product-of-array-except-self

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0] for _ in range(n)]
        suffix = [nums[n - 1] for _ in range(n)]
        answer = [0 for _ in range(n)]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
            suffix[i] = suffix[i - 1] * nums[n - 1 - i]

        suffix.reverse()
        
        for i in range(n):
            if i - 1 >= 0 and i + 1 <= n - 1:
                answer[i] = prefix[i - 1] * suffix [i + 1]
            elif i - 1 < 0:
                answer[i] = suffix[i + 1]
            elif i + 1 > n - 1:
                answer[i] = prefix[i - 1]
            else:
                break

        return answer
        