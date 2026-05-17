# https://leetcode.cn/problems/binary-tree-level-order-traversal-ii

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        from collections import deque

        q = deque()
        q.append(root)
        res = []

        while q:
            size = len(q)
            row = []

            for _ in range(size):
                node = q.popleft()
                row.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(row)

        return res.reverse()
