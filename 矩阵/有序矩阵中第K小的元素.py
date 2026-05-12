# https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix

from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        pq = []
        for index, list_ in enumerate(matrix):
            heapq.heappush(pq, (list_[0], index, 0))
            # (val, index_in_matrix, index in list_)

        for _ in range(k-1):
            _, index, i = heapq.heappop(pq)
            list_ = matrix[index]

            if i + 1 >= len(list_):
                # 检测这一行是否已经全部加完
                continue

            heapq.heappush(pq, (list_[i+1], index, i+1))

        val, _, _ = heapq.heappop(pq)
        return val





