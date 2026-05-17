# https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def traverse(self, root, val):
        if root is None:
            return

        root.val = val
        self.dict[root.val] += 1

        self.traverse(root.left, 2 * val + 1)
        self.traverse(root.right, 2 * val + 2)

    def __init__(self, root: Optional[TreeNode]):
        from collections import defaultdict

        self.dict = defaultdict(int)
        self.traverse(root, 0)

    def find(self, target: int) -> bool:
        return self.dict[target] >= 1