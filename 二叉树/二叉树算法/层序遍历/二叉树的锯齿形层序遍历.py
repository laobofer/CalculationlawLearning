# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        from collections import deque

        q = deque()
        q.append(root)
        direction = False  # 向右
        res = []

        while q:
            size = len(q)
            direction = not direction
            row = []

            for _ in range(size):
                node = q.popleft()
                row.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not direction:
                row.reverse()
            res.append(row)

        return res
