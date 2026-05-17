# https://leetcode.cn/problems/longest-univalue-path

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_num = -float("inf")

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            """返回从 root 开始的路径的节点数"""
            if root is None:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            cur_cum = 1
            if root.left and root.left.val == root.val:
                cur_cum += left
            if root.right and root.right.val == root.val:
                cur_cum += right

            self.max_num = max(cur_cum, self.max_num)

            return max(
                1,
                (1 + left if root.left and root.left.val == root.val else 0),
                (1 + right if root.right and root.right.val == root.val else 0),
            )

        helper(root)

        return self.max_num - 1 if self.max_num > 1 else 0



            

            
