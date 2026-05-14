# https://leetcode.cn/problems/maximum-depth-of-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.depth = 0
        self.max_depth = 0

    def traverse(self, root):
        if root is None:
            return

        self.depth += 1

        if root.left is None and root.right is None:
            self.max_depth = max(self.max_depth, self.depth)

        self.traverse(root.left)
        self.traverse(root.right)

        self.depth -= 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.max_depth