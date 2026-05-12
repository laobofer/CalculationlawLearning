# https://leetcode.cn/problems/min-stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack_min and self.stack_min[-1] >= val:
            self.stack_min.append(val)
        elif not self.stack_min:
            self.stack_min.append(val)
        else:
            self.stack_min.append(self.stack_min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()