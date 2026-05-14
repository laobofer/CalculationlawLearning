# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(root):
            """此函数返回展开后的头"""
            if root is None:
                return None

            if root.left is None and root.right is None:
                return root

            left_head = helper(root.left)
            right_head = helper(root.right)

            root.left = None
            p = left_head

            if p:
                root.right = p
                while p.right:
                    p = p.right
                p.right = right_head
                return root
            else:
                root.right = right_head
                return root

        helper(root)

        return root
