# https://leetcode.cn/problems/time-needed-to-buy-tickets

from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        from collections import deque

        q = deque()
        for i, ticket in enumerate(tickets):
            q.append([i, ticket])

        res = 0
        while True:
            index, ticket = q.popleft()
            ticket -= 1
            res += 1

            if index == k and ticket == 0:
                return res
            
            if ticket == 0:
                continue

            q.append([index, ticket])



