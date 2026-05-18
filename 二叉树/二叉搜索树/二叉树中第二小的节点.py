# https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return -1

        left, right = root.left.val, root.right.val

        if root.val == root.left.val:
            left = self.findSecondMinimumValue(root.left)
        if root.val == root.right.val:
            right = self.findSecondMinimumValue(root.right)

        if left == -1:
            return right
        if right == -1:
            return left
        
        return min(left, right)