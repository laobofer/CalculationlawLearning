# https://leetcode.cn/problems/cousins-in-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.dict = {}
        self.dict[root.val] = [None, 1]

        def helper(root, depth):
            if root is None:
                return

            if root.left:
                self.dict[root.left.val] = [root, depth]
            if root.right:
                self.dict[root.right.val] = [root, depth]

            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 2)

        return (
            self.dict[x][1] == self.dict[y][1]
            and self.dict[x][0] is not self.dict[y][0]
        )
