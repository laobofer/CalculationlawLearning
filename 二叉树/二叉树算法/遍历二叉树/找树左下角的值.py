# https://leetcode.cn/problems/find-bottom-left-tree-value

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            first = q[0].val

            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if len(q) == 0:
                return first
