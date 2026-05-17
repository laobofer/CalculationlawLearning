# https://leetcode.cn/problems/sum-root-to-leaf-numbers

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.nums = []
        self.path = []

    def traverse(self, root):
        if root is None:
            return

        self.path.append(str(root.val))
        if root.left is None and root.right is None:
            num = (
                int("".join(self.path).lstrip("0"))
                if len(self.path) >= 2
                else int(self.path[0])
            )
            if not num:
                num = 0
            self.nums.append(num)

        self.traverse(root.left)
        self.traverse(root.right)

        self.path.pop()

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)

        return sum(self.nums)