# https://leetcode.cn/problems/merge-sorted-array

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1, index_2 = m - 1, n - 1
        index = m + n - 1

        while index_1 >= 0 and index_2 >= 0:
            max_ = -1e10
            if nums1[index_1] >= nums2[index_2]:
                max_ = nums1[index_1]
                index_1 -= 1
            else:
                max_ = nums2[index_2]
                index_2 -= 1

            nums1[index] = max_
            index -= 1

        while index_1 >= 0:
            max_ = nums1[index_1]
            nums1[index] = max_
            index_1 -= 1
            index -= 1

        while index_2 >= 0:
            max_ = nums2[index_2]
            nums1[index] = max_
            index_2 -= 1
            index -= 1

s = Solution()
s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)