# https://leetcode.cn/problems/design-front-middle-back-queue


# 此题用 left 和 right 两个 deque 实现更好

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def pushFront(self, val):
        node = Node(val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def pushMiddle(self, val):
        slow, fast = self.head.next, self.head.next

        while (
            fast and fast.next and fast is not self.tail and fast.next is not self.tail
        ):
            fast = fast.next.next
            slow = slow.next

        node = Node(val)
        node.next = slow
        node.prev = slow.prev
        slow.prev.next = node
        slow.prev = node

    def pushBack(self, val):
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def popFront(self):
        val = self.head.next.val
        node = self.head.next.next
        self.head.next = node
        node.prev = self.head
        return val

    def popMiddle(self):
        slow, fast = self.head.next, self.head.next
        while (
            fast and fast.next and fast is not self.tail and fast.next is not self.tail
        ):
            fast = fast.next.next
            slow = slow.next

        if fast is self.tail:
            slow = slow.prev

        val = slow.val
        next = slow.next
        prev = slow.prev
        next.prev = prev
        prev.next = next

        return val

    def popBack(self):
        val = self.tail.prev.val
        node = self.tail.prev.prev

        node.next = self.tail
        self.tail.prev = node
        return val


class FrontMiddleBackQueue:
    def __init__(self):
        self.q = LinkedList()
        self.size = 0

    def pushFront(self, val: int) -> None:
        self.q.pushFront(val)
        self.size += 1

    def pushMiddle(self, val: int) -> None:
        self.q.pushMiddle(val)
        self.size += 1

    def pushBack(self, val: int) -> None:
        self.q.pushBack(val)
        self.size += 1

    def _isEmpty(self):
        return self.size == 0

    def popFront(self) -> int:
        if self._isEmpty():
            return -1

        self.size -= 1
        return self.q.popFront()

    def popMiddle(self) -> int:
        if self._isEmpty():
            return -1

        self.size -= 1
        return self.q.popMiddle()

    def popBack(self) -> int:
        if self._isEmpty():
            return -1

        self.size -= 1
        return self.q.popBack()
        
