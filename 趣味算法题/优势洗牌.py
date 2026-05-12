# https://leetcode.cn/problems/advantage-shuffle

from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_with_index = sorted([[num, index] for index, num in enumerate(nums2)], key=lambda x: x[0])

        nums1_sorted = sorted(nums1)
        res = [0 for _ in range(len(nums1))]

        left, right = 0, len(nums1_sorted) - 1
        index = len(nums1_sorted) - 1
        
        while index >= 0:
            if nums2_with_index[index][0] >= nums1_sorted[right]:
                i = nums2_with_index[index][1]
                res[i] = nums1_sorted[left]
                left += 1
            else:
                i = nums2_with_index[index][1]
                res[i] = nums1_sorted[right]
                right -= 1

            index -= 1

        return res

print(Solution().advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))

