# https://leetcode.cn/problems/maximum-frequency-stack


class FreqStack:
    def __init__(self):
        from collections import defaultdict

        self.max_freq = 0
        self.v2f = defaultdict(int)
        self.f2v = defaultdict(list)

    def push(self, val: int) -> None:
        self.v2f[val] += 1
        self.max_freq = max(self.max_freq, self.v2f[val])
        self.f2v[self.v2f[val]].append(val)

    def pop(self) -> int:
        val = self.f2v[self.max_freq].pop()

        self.v2f[val] -= 1
        if not self.f2v[self.max_freq]:
            self.max_freq -= 1

        if not self.f2v[self.max_freq]:
            del self.f2v[self.max_freq]
        if self.v2f[val] == 0:
            del self.v2f[val]

        return val


