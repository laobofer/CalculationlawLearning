# https://leetcode.cn/problems/flip-equivalent-binary-trees

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root1, root2):
            if root1 is None and root2 is None:
                return True

            if root1 is None and root2 is not None:
                return False

            if root1 is not None and root2 is None:
                return False

            if root1.val != root2.val:
                return False

            root1_left = root1.left.val if root1.left else -1
            root1_right = root1.right.val if root1.right else -1
            root2_left = root2.left.val if root2.left else -1
            root2_right = root2.right.val if root2.right else -1

            if root1_left == root2_right and root1_right == root2_left:
                root2.left, root2.right = root2.right, root2.left

            left = helper(root1.left, root2.left)
            right = helper(root1.right, root2.right)

            return left and right and root1.val == root2.val

        return helper(root1, root2)