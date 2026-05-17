# https://leetcode.cn/problems/merge-two-binary-trees

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """合并并返回此树的头结点"""
        if root1 is None and root2 is None:
            return None
        
        left, right = None, None
        if root1 is None:        
            left = self.mergeTrees(None, root2.left)
            right = self.mergeTrees(None, root2.right)

        if root2 is None:
            left = self.mergeTrees(root1.left, None)
            right = self.mergeTrees(root1.right, None)     

        if root1 and root2:
            left = self.mergeTrees(root1.left, root2.left)
            right = self.mergeTrees(root1.right, root2.right)                

        root1_val = root1.val if root1 else 0
        root2_val = root2.val if root2 else 0

        root = TreeNode(
            root1_val + root2_val,
            left, 
            right
        )

        return root