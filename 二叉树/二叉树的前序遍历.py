# https://leetcode.cn/problems/binary-tree-preorder-traversal

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ret = []

    def traverse(self, root):
        if root is None:
            return
        
        self.ret.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)

        return self.ret