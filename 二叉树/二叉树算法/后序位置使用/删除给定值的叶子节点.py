# https://leetcode.cn/problems/delete-leaves-with-a-given-value

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(root, target):
            """返回删除所有 target 叶子节点后的子树的根节点"""
            if root is None:
                return None
            
            left = helper(root.left, target)
            right = helper(root.right, target)

            root.left = left
            root.right = right

            if root.left is None and root.right is None and root.val == target:
                root = None

            return root
        
        return helper(root, target)

            