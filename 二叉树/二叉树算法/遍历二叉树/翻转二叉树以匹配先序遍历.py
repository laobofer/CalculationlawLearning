# https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []
        self.isValid = True
        self.i = 0

    def traverse(self, root, voyage):
        if root is None or not self.isValid:
            return

        if root.val != voyage[self.i]:
            self.isValid = False
            return

        self.i += 1

        if root.left and root.left.val != voyage[self.i]:
            self.res.append(root.val)
            root.left, root.right = root.right, root.left

        self.traverse(root.left, voyage)
        self.traverse(root.right, voyage)

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.traverse(root, voyage)

        return self.res if self.isValid else [-1]


Solution().flipMatchVoyage(TreeNode(1, TreeNode(2), TreeNode(3)), [1, 3, 2])