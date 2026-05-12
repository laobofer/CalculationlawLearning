# https://leetcode.cn/problems/implement-queue-using-stacks

class MyQueue:
    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.queue:
            return self.queue.pop()

        while self.stack:
            self.queue.append(self.stack.pop())
        return self.queue.pop()

    def peek(self) -> int:
        return self.stack[0] if not self.queue else self.queue[-1]

    def empty(self) -> bool:
        return not self.queue and not self.stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()