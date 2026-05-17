# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None:
            return root

        from collections import deque

        q = deque()
        q.append(root)

        while q:
            size = len(q)

            for _ in range(size - 1):
                node = q.popleft()
                node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            node = q.popleft()
            node.next = None
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root