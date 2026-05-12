# https://leetcode.cn/problems/contains-duplicate-ii

from typing import List

class Solution:
    def need_shrink(self, left, right, k):
        return right - left > k

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict

        window = defaultdict(int)

        left, right = 0, 0

        while right < len(nums):
            num = nums[right]
            window[num] += 1
            right += 1


            while left < right and self.need_shrink(left, right, k):
                num_ = nums[left]
                window[num_] -= 1
                left += 1

            if window[num] > 1:
                return True

        return False
            
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))

# 正确但性能不佳

# class Solution:
#     def need_shrink(self, left, right, k):
#         return right - left > k + 1

#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         from collections import defaultdict

#         window = defaultdict(int)

#         left, right = 0, 0

#         while right < len(nums):
#             num = nums[right]
#             window[num] += 1
#             right += 1

#             while left < right and self.need_shrink(left, right, k):
#                 num = nums[left]
#                 window[num] -= 1
#                 left += 1

#             if any([True if num >= 2 else False for number, num in window.items()]):
#                 return True

#         return False