# https://leetcode.cn/problems/find-k-pairs-with-smallest-sums

from typing import List


# 可行, 但超出内存限制, 应当动态展开而不是全部生成
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         import heapq
#         martix = [[] for _ in range(len(nums1))]
#         ret = []

#         pq = []

#         for index, num1 in enumerate(nums1):
#             for num2 in nums2:
#                 # 和, 数1, 数2
#                 martix[index].append((num1 + num2, num1, num2))
#             sum, num1, num2 = martix[index][0]
#             heapq.heappush(pq, (sum, num1, num2, index, 0))

#         for _ in range(k):
#             _, num1, num2, index, i = heapq.heappop(pq)
#             ret.append([num1, num2])

#             if i + 1 >= len(martix[index]):
#                 continue

#             heapq.heappush(
#                 pq,
#                 (
#                     martix[index][i + 1][0],
#                     martix[index][i + 1][1],
#                     martix[index][i + 1][2],
#                     index,
#                     i + 1,
#                 ),
#             )

#         return ret


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        import heapq
        
        len_ = len(nums2)
        ret = []
        pq = []

        for num1 in nums1:
            heapq.heappush(pq, (num1 + nums2[0], num1, nums2[0], 0))

        for _ in range(k):
            _, num1, num2, i = heapq.heappop(pq)

            ret.append([num1, num2])

            if i + 1 >= len_:
                continue

            heapq.heappush(pq, (num1 + nums2[i + 1], num1, nums2[i + 1], i + 1))

        return ret

# s = Solution()
# print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))




