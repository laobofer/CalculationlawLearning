# https://leetcode.cn/problems/average-of-levels-in-binary-tree

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return 0
        
        from collections import deque
        q = deque()
        q.append(root)
        res = []

        while q:
            size = len(q)
            _sum = 0

            for _ in range(size):
                node = q.popleft()
                _sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(_sum / size)

        return res