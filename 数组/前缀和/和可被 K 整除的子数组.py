# https://leetcode.cn/problems/subarray-sums-divisible-by-k

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums) + 1
        preSum = [0 for _ in range(n)]

        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        from collections import defaultdict
        dict = defaultdict(list)

        for i in range(n):
            dict[preSum[i] % k].append(i)
        
        res = 0
        for i in range(1, n):
            need = preSum[i] % k
            if need in dict:
                res += sum(1 for index in dict[need] if index < i)

        return res


# from typing import List
# import bisect


# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         n = len(nums) + 1
#         preSum = [0] * n

#         for i in range(1, n):
#             preSum[i] = preSum[i - 1] + nums[i - 1]

#         # 先构建完整哈希表：余数 -> 下标列表（有序）
#         dict = {}
#         for i in range(n):
#             mod = preSum[i] % k
#             if mod not in dict:
#                 dict[mod] = []
#             dict[mod].append(i)

#         res = 0
#         for i in range(1, n):
#             need = preSum[i] % k
#             if need in dict:
#                 # 优化：二分查找 < i 的数量
#                 cnt = bisect.bisect_left(dict[need], i)
#                 res += cnt

#         return res

# from typing import List
# from collections import defaultdict


# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         pre_sum = 0
#         res = 0
#         count = defaultdict(int)
#         count[0] = 1  # 关键初始化

#         for num in nums:
#             pre_sum += num
#             # 计算余数（Python 自动处理负数）
#             mod = pre_sum % k
#             # 前面出现过多少次同余 = 多少个合法子数组
#             res += count[mod]
#             count[mod] += 1

#         return res