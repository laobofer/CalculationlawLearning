# https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 1

        from collections import deque

        q = deque()
        q.append(root)
        max_sum = [-float("inf"), -1]
        depth = 0

        while q:
            size = len(q)
            _sum = 0
            depth += 1

            for _ in range(size):
                node = q.popleft()
                _sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if _sum > max_sum[0]:
                max_sum = [_sum, depth]

        return max_sum[1]