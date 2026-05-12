# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node

from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# 也可以用遍历的方式做, 把连起来的每条指针看作是一个分支, 遍历三叉树

class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        from collections import deque

        if not root:
            return root

        q = deque()
        q.append(root)

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

        return root
