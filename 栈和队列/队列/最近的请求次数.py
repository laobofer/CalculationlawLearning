# https://leetcode.cn/problems/number-of-recent-calls

class RecentCounter:

    def __init__(self):
        from collections import deque
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)

        while t - self.q[0] > 3000:
            self.q.popleft()

        return len(self.q)
