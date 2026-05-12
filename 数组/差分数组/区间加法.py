# 竟然是 VIP 的题, 太可恶了

from typing import List

class Solution:
    def increase(self, diff, start_index, end_index, inc):
        if start_index >= 0 and start_index < len(diff):
            diff[start_index] += inc
        
        if end_index + 1 < len(diff):
            diff[end_index + 1] -= inc

    def get_nums(self, diff):
        res = []
        
        res.append(diff[0])
        for i in range(1, len(diff)):
            res.append(diff[i] + res[i - 1])

        return res

    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0 for _ in range(length)]
        for update in updates:
            start_index, end_index, inc = update
            self.increase(diff, start_index, end_index, inc)

        return self.get_nums(diff)

sol = Solution()
print(sol.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))  # [-2, 0, 3, 5, 3]
