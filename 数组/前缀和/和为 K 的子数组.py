# https://leetcode.cn/problems/subarray-sum-equals-k

from typing import List
import bisect

# 这里不加二分查找库则过不了测试

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums) + 1
        preSum = [0] * n

        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        # 第一步：先构建完整哈希表（值 -> 下标列表，有序）
        pos = {}
        for idx in range(n):
            val = preSum[idx]
            if val not in pos:
                pos[val] = []
            pos[val].append(idx)  # 下标一定从小到大，保持有序

        res = 0
        for i in range(1, n):
            need = preSum[i] - k
            if need in pos:
                # 优化点：bisect 直接算出有多少个 index < i
                cnt = bisect.bisect_left(pos[need], i)
                res += cnt

        return res
    
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         n = len(nums) + 1
#         preSum = [0 for _ in range(n)]

#         for i in range(1, n):
#             preSum[i] = preSum[i - 1] + nums[i - 1]

#         dict = {}
#         # 记录 preSum[i] -> [i1, i2, ...] 的哈希表

#         for i in range(n):
#             if preSum[i] not in dict:
#                 dict[preSum[i]] = [i]
#             else:
#                 dict[preSum[i]].append(i)

#         res = 0
#         print(dict)
#         for i in range(1, n):
#             need = preSum[i] - k
#             if need in dict:
#                 res += sum([1 if index < i else 0 for index in dict[need]])

#         return res

    
# 好一些的想法, 边遍历边计数, 可以自动维护范围, 使之不重复

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         n = len(nums) + 1
#         preSum = [0] * n

#         for i in range(1, n):
#             preSum[i] = preSum[i - 1] + nums[i - 1]

#         # 第一步：先构建完整哈希表（值 -> 下标列表，有序）
#         pos = {}
#         for idx in range(n):
#             val = preSum[idx]
#             if val not in pos:
#                 pos[val] = []
#             pos[val].append(idx)  # 下标一定从小到大，保持有序

#         res = 0
#         for i in range(1, n):
#             need = preSum[i] - k
#             if need in pos:
#                 # 优化点：bisect 直接算出有多少个 index < i
#                 cnt = bisect.bisect_left(pos[need], i)
#                 res += cnt

#         return res