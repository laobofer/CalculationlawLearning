# https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero

from typing import List

class Solution:
    def need_shrink(self, window, need):
        return window >= need
    
    def minOperations(self, nums: List[int], x: int) -> int:
        window = 0
        need = sum(nums) - x

        if need == 0:
            return len(nums)

        left, right = 0, 0
        res = [0, 0]

        while right < len(nums):
            num = nums[right]
            window += num
            right += 1

            while left < right and self.need_shrink(window, need):
                if window == need:
                    res = (
                        [left, right]
                        if right - left > res[1] - res[0] or res == [0, 0]
                        else res
                    )
                
                num = nums[left]
                window -= num
                left += 1                

        return len(nums) - (res[1] - res[0]) if res != [0, 0] else -1

print(Solution().minOperations(
    [
        8828,
        9581,
        49,
        9818,
        9974,
        9869,
        9991,
        10000,
        10000,
        10000,
        9999,
        9993,
        9904,
        8819,
        1231,
        6309,
    ],
    134365
))


# 这样做更好, 内部的 while 执行完之后, window 是 <= target 的, 此时判断无需考虑 target == 0 时的情况

# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         n = len(nums)
#         sum_ = sum(nums)
#         # 滑动窗口需要寻找的子数组目标和
#         target = sum_ - x

#         left = 0
#         right = 0
#         # 记录窗口内所有元素和
#         window_sum = 0
#         # 记录目标子数组的最大长度
#         max_len = float("-inf")
#         # 开始执行滑动窗口框架
#         while right < n:
#             # 扩大窗口
#             window_sum += nums[right]
#             right += 1

#             while window_sum > target and left < right:
#                 # 缩小窗口
#                 window_sum -= nums[left]
#                 left += 1

#             # 寻找目标子数组
#             if window_sum == target:
#                 max_len = max(max_len, right - left)

#         # 目标子数组的最大长度可以推导出需要删除的字符数量
#         return -1 if max_len == float("-inf") else n - max_len