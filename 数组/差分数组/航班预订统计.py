# https://leetcode.cn/problems/corporate-flight-bookings

from typing import List

class Solution:
    def increase(self, diff, start_index, end_index, inc):
        if start_index >= 0 and start_index < len(diff):
            diff[start_index] += inc

        if end_index + 1 < len(diff):
            diff[end_index + 1] -= inc

    def get_nums(self, diff):
        res = [diff[0] for _ in range(len(diff))]

        for i in range(1, len(diff)):
            res[i] = res[i - 1] + diff[i]

        return res

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0 for i in range(n)]

        for booking in bookings:
            start_index, end_index, inc = booking
            self.increase(diff, start_index - 1, end_index - 1, inc)

        return self.get_nums(diff)

Solution().corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)