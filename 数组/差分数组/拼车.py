# https://leetcode.cn/problems/car-pooling 

from typing import List

class Solution:
    def increase(self, diff, start_index, end_index, inc):
        if start_index >= 0 and start_index < len(diff):
            diff[start_index] += inc

        if end_index + 1 < len(diff):
            diff[end_index] -= inc

    def get_nums(self, diff):
        res = [diff[0] for _ in range(len(diff))]

        for i in range(1, len(diff)):
            res[i] = res[i - 1] + diff[i]

        return res

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0 for _ in range(1000 + 1)]

        for trip in trips:
            inc, start_index, end_index = trip
            self.increase(diff, start_index, end_index, inc)

        return max(self.get_nums(diff)) <= capacity

