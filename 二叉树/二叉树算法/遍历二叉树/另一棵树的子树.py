# https://leetcode.cn/problems/subtree-of-another-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = False

    def _isSame(self, root, subRoot):
        """返回两棵树是不是相同"""
        if root is None and subRoot:
            return False
        if root and subRoot is None:
            return False
        if root is None and subRoot is None:
            return True

        left = self._isSame(root.left, subRoot.left)
        right = self._isSame(root.right, subRoot.right)

        return left and right and root.val == subRoot.val

    def traverse(self, root, subRoot):
        if root is None:
            return

        if root.val == subRoot.val:
            self.res = self._isSame(root, subRoot) if not self.res else True

        self.traverse(root.left, subRoot)
        self.traverse(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.traverse(root, subRoot)

        return self.res