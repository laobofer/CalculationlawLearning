# https://leetcode.cn/problems/peak-index-in-a-mountain-array

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if left == right:
                return left
            
            if arr[mid] > arr[mid + 1]:
                right = mid
            elif arr[mid] < arr[mid + 1]:
                left = mid + 1

        return left