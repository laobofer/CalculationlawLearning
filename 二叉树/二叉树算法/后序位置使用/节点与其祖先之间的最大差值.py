# https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max = -float("inf")

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            """返回: 以 root 为根的子树的最小值, 以 root 为根的子树的最大值"""
            if root is None:
                return float("inf"), -float("inf")

            l_min, l_max = helper(root.left)
            r_min, r_max = helper(root.right)

            self.max = max(
                self.max,
                abs(root.val - min(l_min, r_min, root.val)),
                abs(root.val - max(l_max, r_max, root.val))
            )

            return min(l_min, r_min, root.val), max(l_max, r_max, root.val)

        helper(root)
        return self.max

