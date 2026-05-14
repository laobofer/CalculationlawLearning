# https://leetcode.cn/problems/delete-node-in-a-bst

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """删除值为 key 的节点, 并返回此时的头结点"""
        if root is None:
            return None
        
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is None:
                return root.left
            else:
                p = root.right
                while p.left is not None:
                    p = p.left

                root.right = self.deleteNode(root.right, p.val)
                p.left = root.left
                p.right = root.right
                root = p
            

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root