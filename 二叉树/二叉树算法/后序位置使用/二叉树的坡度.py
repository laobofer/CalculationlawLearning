# https://leetcode.cn/problems/binary-tree-tilt

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            """返回: 以 root 为根的子树之和, 以 root 为根的子树的坡度"""
            if root is None:
                return 0, 0

            l_sum, l_tilt = helper(root.left)
            r_sum, r_tilt = helper(root.right)

            return l_sum + r_sum + root.val, abs(l_sum - r_sum) + l_tilt + r_tilt

        _, res = helper(root)

        return res