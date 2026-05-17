# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder, inorder):
            if len(preorder) == 0:
                return None

            root_val = preorder[0]
            index = inorder.index(root_val)

            len_left = index

            left = helper(preorder[1 : 1 + len_left], inorder[0:index])
            right = helper(preorder[1 + len_left :], inorder[index + 1 :])

            root = TreeNode(root_val, left, right)

            return root

        return helper(preorder, inorder)