# https://leetcode.cn/problems/recover-binary-search-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.nodes = []

    def traverse(self, root):
        if root is None:
            return

        self.traverse(root.left)
        self.nodes.append(root)
        self.traverse(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        lst = [node.val for node in self.nodes]
        lst.sort()
        pair = []

        for val, node in zip(lst, self.nodes):
            if val != node.val:
                pair.append(node)

        pair[0].val, pair[1].val = pair[1].val, pair[0].val



