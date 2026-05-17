# https://leetcode.cn/problems/leaf-similar-trees

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.leaf1 = []
        self.leaf2 = []

    def traverse(self, root, id):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            if id == 1:
                self.leaf1.append(root.val)
            else:
                self.leaf2.append(root.val)

        self.traverse(root.left, id)
        self.traverse(root.right, id)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.traverse(root1, 1)
        self.traverse(root2, 2)

        return self.leaf1 == self.leaf2