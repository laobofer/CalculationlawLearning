# https://leetcode.cn/problems/find-largest-value-in-each-tree-row

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        from collections import deque

        q = deque()
        q.append(root)

        res = []
        while q:
            size = len(q)
            _max = -float("inf")

            for _ in range(size):
                node = q.popleft()
                if node.val > _max:
                    _max = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(_max)

        return res
