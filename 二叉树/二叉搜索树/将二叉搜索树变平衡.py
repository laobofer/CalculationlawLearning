# https://leetcode.cn/problems/balance-a-binary-search-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.lst = []

        def traverse(root):
            if root is None:
                return

            traverse(root.left)
            self.lst.append(root.val)
            traverse(root.right)

        traverse(root)

        return self.sortedArrayToBST(self.lst)

    def sortedArrayToBST(self, nums):
        def helper(lo, hi):
            if lo >= hi:
                return None

            _len = hi - lo
            index = _len // 2 + lo
            root_val = nums[index]

            left = helper(lo, index)
            right = helper(index + 1, hi)

            root = TreeNode(root_val, left, right)

            return root

        return helper(0, len(nums))