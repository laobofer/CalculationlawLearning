# https://leetcode.cn/problems/next-greater-element-i

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res_2 = [0 for _ in range(n)]
        res = []
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            res_2[i] = -1 if not stack else stack[-1]
            stack.append(nums2[i])

        for num in nums1:
            res.append(res_2[nums2.index(num)])

        return res
