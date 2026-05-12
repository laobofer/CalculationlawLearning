# https://leetcode.cn/problems/online-stock-span

class StockSpanner:
    def __init__(self):
        self.stack = []
        self.index = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        res = self.index if not self.stack else self.index - self.stack[-1][1]
        res += 1

        self.index += 1
        self.stack.append([price, self.index])

        return res
