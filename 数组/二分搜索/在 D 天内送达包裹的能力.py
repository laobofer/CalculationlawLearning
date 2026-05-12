# https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days

from typing import List

class Solution:
    def get_needed_days(self, weights, ship_cap):
        temp_storage = 0
        res = 0

        for weight in weights:
            temp_storage += weight
            if temp_storage > ship_cap:
                temp_storage = weight
                res += 1
            elif temp_storage == ship_cap:
                temp_storage = 0
                res += 1

        if temp_storage != 0:
            res += 1

        return res

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), 50000 * 500

        while left <= right:
            mid = left + (right - left) // 2
            needed_days = self.get_needed_days(weights, mid)
            if needed_days < days:
                right = mid - 1
            elif needed_days == days:
                right = mid - 1
            elif needed_days > days:
                left = mid + 1

        return left
    

print(Solution().get_needed_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15], 15))
