# https://leetcode.cn/problems/validate-binary-search-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            # 此函数返回: (是否是合法的 BST, 以此节点为根的子树的最大值, 以此节点为根的子树的最小值)
            if root is None:
                return True, -float("inf"), float("inf")

            left, max_l, min_l = helper(root.left)
            right, max_r, min_r = helper(root.right)

            this = max_l < root.val < min_r

            return (
                this and left and right,
                max(max_l, max_r, root.val),
                min(min_l, min_r, root.val),
            )

        res, _, _ = helper(root)
        return res
        

# 用中序遍历实现更好
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None

        def inorder(node):
            if not node:
                return True

            if not inorder(node.left):
                return False

            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val

            return inorder(node.right)

        return inorder(root)