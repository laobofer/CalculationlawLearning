# https://leetcode.cn/problems/construct-string-from-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(root):
            if root is None:
                return ''
            
            left = helper(root.left)
            right = helper(root.right)

            return (
                str(root.val) + "(" + left + ")" + "(" + right + ")"
                if left and right
                else str(root.val) + "(" + left + ")"
                if left and not right
                else str(root.val) + "(" + ")" + "(" + right + ")"
                if not left and right
                else str(root.val)
            )
        
        return helper(root)