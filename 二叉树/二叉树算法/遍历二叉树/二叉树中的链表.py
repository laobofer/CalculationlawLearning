# https://leetcode.cn/problems/linked-list-in-binary-tree

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = False
        self.path = []

    def _is_suffix(self, list_a, list_b):
        return len(list_b) <= len(list_a) and all(
            a == b for a, b in zip(reversed(list_a), reversed(list_b))
        )

    def traverse(self, root, lst):
        if root is None or self.res:
            return

        self.path.append(root.val)

        self.res = self._is_suffix(self.path, lst)

        self.traverse(root.left, lst)
        self.traverse(root.right, lst)

        self.path.pop()

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next

        self.traverse(root, lst)
        return self.res
