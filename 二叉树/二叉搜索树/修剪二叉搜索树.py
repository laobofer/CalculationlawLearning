# https://leetcode.cn/problems/trim-a-binary-search-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def helper(root):
            """返回删除对应节点之后的头结点"""
            if root is None:
                return None
            
            if root.val < low:
                return helper(root.right)
            if root.val > high:
                return helper(root.left)
            
            left = helper(root.left)
            right = helper(root.right)

            root.left = left
            root.right = right
            return root
        return helper(root)