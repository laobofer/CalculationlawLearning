# https://leetcode.cn/problems/binary-tree-pruning

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            """返回此子树是否含有 1"""
            if root is None:
                return False

            left = helper(root.left)
            right = helper(root.right)

            if left is False:
                root.left = None

            if right is False:
                root.right = None

            return left or right or root.val == 1

        if not helper(root):
            root = None
        return root