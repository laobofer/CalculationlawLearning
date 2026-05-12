# https://leetcode.cn/problems/design-circular-deque


class LinkedNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = LinkedNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertFront(self, val):
        node = LinkedNode(val, self.head, self.head.next)
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def insertLast(self, val):
        node = LinkedNode(val, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def deleteFront(self):
        node = self.head.next.next
        self.head.next = node
        node.prev = self.head
        self.size -= 1

        return True

    def deleteLast(self):
        node = self.tail.prev.prev
        self.tail.prev = node
        node.next = self.tail
        self.size -= 1

        return True

    def getFront(self):
        return self.head.next.val

    def getRear(self):
        return self.tail.prev.val


class MyCircularDeque:
    def __init__(self, k: int):
        self.linkedlist = LinkedList()
        self.size = 0
        self.cap = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.linkedlist.insertFront(value)
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.linkedlist.insertLast(value)
        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.linkedlist.deleteFront()
        self.size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.linkedlist.deleteLast()
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.linkedlist.getFront()

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.linkedlist.getRear()

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap