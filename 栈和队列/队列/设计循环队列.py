# https://leetcode.cn/problems/design-circular-queue

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1 for _ in range(k)]
        self.left, self.right = 0, 0
        self.cap = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q[self.right] = value
        self.size += 1
        self.right = (self.right + 1) % self.cap

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.q[self.left] = -1
        self.size -= 1
        self.left = (self.left + 1) % self.cap

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        val = self.q[self.left]
        return val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        index = (self.right - 1 + self.cap) % self.cap
        val = self.q[index]

        return val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap