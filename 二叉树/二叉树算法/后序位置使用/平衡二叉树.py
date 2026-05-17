# https://leetcode.cn/problems/balanced-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = True

    def get_depth(self, root):
        """返回此节点对应子树的深度"""
        if not self.res:
            return 0

        if root is None:
            return 0
        
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)

        if abs(left - right) > 1:
            self.res = False

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.get_depth(root)

        return self.res