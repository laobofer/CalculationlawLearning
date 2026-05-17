# https://leetcode.cn/problems/sum-of-nodes-with-even-valued-grandparent

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def count_ont_node(self, root):
        res = 0
        if root.left:
            if root.left.left:
                res += root.left.left.val
            if root.left.right:
                res += root.left.right.val

        if root.right:
            if root.right.left:
                res += root.right.left.val
            if root.right.right:
                res += root.right.right.val

        return res

    def traverse(self, root):
        if root is None:
            return
        
        if root.val % 2 ==0:
            self.count += self.count_ont_node(root)

        self.traverse(root.left)
        self.traverse(root.right)

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.count
