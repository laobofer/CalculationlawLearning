# https://leetcode.cn/problems/diameter-of-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0

    def traverse(self, root):
        if root is None:
            return
        
        self.max_diameter = max(root.l_depth + root.r_depth, self.max_diameter)

        self.traverse(root.left)
        self.traverse(root.right)

    def max_depth(self, root):
        if root is None:
            return 0
        
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        root.l_depth = left
        root.r_depth = right

        return 1 + max(left, right)
        


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth(root)
        self.traverse(root)

        return self.max_diameter