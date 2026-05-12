# https://leetcode.cn/problems/contains-duplicate-iii

from typing import List

# 如何判断两数的值的差在合适的范围中
# 一种可行的方法是桶
# 这里可以进一步把 list 优化成 [min, max], 这样可以不要 bisect

class Solution:
    def need_shrink(self, left, right, indexDiff):
        return right - left > indexDiff

    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        import bisect
        from collections import defaultdict
        window = defaultdict(list)
        width = valueDiff + 1
        left, right = 0, 0

        while right < len(nums):
            num = nums[right]
            bid = num // width
            if bid in window:
                return True
            if bid - 1 in window and num - window[bid - 1][-1] <= valueDiff:
                return True
            if bid + 1 in window and window[bid + 1][0] - num <= valueDiff:
                return True

            bisect.insort_left(
                window[bid], num
            )
            right += 1

            while left < right and self.need_shrink(left, right, indexDiff):
                num = nums[left]
                bid = num // width

                if bid in window and num in window[bid]:
                    window[bid].remove(num)
                    if len(window[bid]) == 0:
                        del window[bid]

                left += 1

        return False
    
# 无法快速得到两个数的差值
# class Solution:
#     def need_shrink(self, left, right, indexDiff):
#         return right - left > indexDiff

#     def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
#         from collections import defaultdict
#         window = defaultdict(int)

#         left, right = 0, 0 
        
#         while right < len(nums):
#             num = nums[right]
#             for key in range(num - valueDiff, num + valueDiff + 1):
#                 if key in window:
#                     return True
#             window[num] += 1
#             right += 1

#             while left < right and self.need_shrink(left, right, indexDiff):
#                 num = nums[left]
#                 window[num] -= 1
#                 if window[num] == 0:
#                     del window[num]
#                 left += 1
            
#         return False
    

print(Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))

# 涉及排序, 速度太慢
# class Solution:
#     def need_shrink(self, left, right, indexDiff):
#         return right - left > indexDiff + 1

#     def containsNearbyAlmostDuplicate(
#         self, nums: List[int], indexDiff: int, valueDiff: int
#     ) -> bool:
#         from collections import defaultdict

#         window = defaultdict(int)

#         left, right = 0, 0

#         while right < len(nums):
#             num = nums[right]
#             window[num] += 1
#             right += 1

#             while left < right and self.need_shrink(left, right, indexDiff):
#                 num = nums[left]
#                 window[num] -= 1
#                 if window[num] == 0:
#                     del window[num]
#                 left += 1

#             keys = [key for key, val in window.items() for _ in range(val)]
#             keys.sort()
#             diff = [abs(keys[i] - keys[i - 1]) for i in range(1, len(keys))]

#             if diff and min(diff) <= valueDiff:
#                 return True

#         return False