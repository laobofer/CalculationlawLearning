# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(inorder, postorder):
            """返回这一段的头结点"""
            assert len(inorder) == len(postorder)

            if len(inorder) == 0:
                return None

            root_val = postorder[-1]
            index = inorder.index(root_val)

            len_left = index

            left = helper(inorder[0:index], postorder[0:index])
            right = helper(
                inorder[index + 1 :], postorder[len_left : len(postorder) - 1]
            )

            root = TreeNode(root_val, left, right)

            return root

        return helper(inorder, postorder)