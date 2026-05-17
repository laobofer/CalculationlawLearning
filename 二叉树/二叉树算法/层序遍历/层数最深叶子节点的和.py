# https://leetcode.cn/problems/deepest-leaves-sum

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        from collections import deque
        q = deque()
        q.append(root)
        res = -1
        
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

            if not q:
                res = _sum

        return res
