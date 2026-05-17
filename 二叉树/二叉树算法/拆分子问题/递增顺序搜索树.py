# https://leetcode.cn/problems/increasing-order-search-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            """返回处理好一个子树后的根节点"""
            if root is None:
                return None

            left = helper(root.left)
            right = helper(root.right)

            root.left = None

            p = left
            if p is None:
                root.right = right
                return root
            else:
                while p.right:
                    p = p.right

                p.right = root
                root.right = right
                return left

        return helper(root)

