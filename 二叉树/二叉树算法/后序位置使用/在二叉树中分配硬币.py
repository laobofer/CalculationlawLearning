# https://leetcode.cn/problems/distribute-coins-in-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def helper(root):
            """
            返回: 这棵二叉树中多出的硬币个数, 负数表示缺少
            """
            if root is None:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            self.res += abs(left) + abs(right)

            return left + right + (root.val - 1)

        helper(root)

        return self.res


                