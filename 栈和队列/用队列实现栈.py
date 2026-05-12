# https://leetcode.cn/problems/implement-stack-using-queues

class MyStack:

    def __init__(self):
        from collections import deque
        self.q = deque()
        self.top_val = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_val = x

    def pop(self) -> int:
        size = len(self.q)
        while size > 1:
            self.q.append(self.q.popleft())
            size -= 1
        res = self.q.popleft()
        self.top_val = self.q[0]

        return res

    def top(self) -> int:
        return self.top_val
        

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()