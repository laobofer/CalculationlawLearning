# https://leetcode.cn/problems/longest-well-performing-interval

from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours) + 1
        preSum = [0 for _ in range(n)]

        for i in range(1, n):
            preSum[i] = preSum[i - 1] + (1 if hours[i - 1] > 8 else -1)

        from collections import defaultdict
        dict = defaultdict(list)
        # 记录 总折合天数 到 index 的映射

        for i in range(n):
            dict[preSum[i]].append(i)
        
        res = 0
        for i in range(1, n):
            need = preSum[i] - 1
            if preSum[i] > 0:
                res = max(res, i)
            if need in dict:
                res = max(res, i - dict[need][0])

        return res

Solution().longestWPI([9, 9, 6, 0, 6, 6, 9])