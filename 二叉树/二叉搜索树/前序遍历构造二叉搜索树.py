# https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(lo, hi):
            if lo >= hi:
                return None

            root_val = preorder[lo]
            index = -1
            for i, val in enumerate(preorder[lo:hi]):
                if val > root_val:
                    index = i
                    break

            index = index + lo if index != -1 else hi

            left = helper(lo + 1, index)
            right = helper(index, hi)

            root = TreeNode(root_val, left, right)
            return root

        return helper(0, len(preorder))
