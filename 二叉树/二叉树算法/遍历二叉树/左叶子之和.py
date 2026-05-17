# https://leetcode.cn/problems/sum-of-left-leaves

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root, is_left):
            """返回: 左叶子"""
            if root is None:
                return 0

            left = helper(root.left, True)
            right = helper(root.right, False)

            isLeaf = root.left is None and root.right is None

            return left + right if not isLeaf else root.val if is_left else 0

        res = helper(root, False)
        return res
