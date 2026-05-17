# https://leetcode.cn/problems/symmetric-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(root1, root2):
            if root1 is None and root2 is not None:
                return False
            if root1 is not None and root2 is None:
                return False
            
            if root1 is None and root2 is None:
                return True
            
            left = helper(root1.left, root2.right)
            right = helper(root1.right, root2.left)

            return left and right and root1.val == root2.val
        
        if root.left is None and root.right is not None:
            return False
        if root.left is not None and root.right is None:
            return False
        
        return help(root.left, root.right)
