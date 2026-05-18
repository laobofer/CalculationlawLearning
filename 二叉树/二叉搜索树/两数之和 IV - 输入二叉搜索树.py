# https://leetcode.cn/problems/two-sum-iv-input-is-a-bst

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.lst = []

        def traverse(root):
            if root is None:
                return

            traverse(root.left)

            self.lst.append(root.val)

            traverse(root.right)

        traverse(root)

        left, right = 0, len(self.lst) - 1

        while left < right:
            if self.lst[left] + self.lst[right] == k:
                return True
            elif self.lst[left] + self.lst[right] < k:
                left += 1
            else:
                right -= 1

        return False