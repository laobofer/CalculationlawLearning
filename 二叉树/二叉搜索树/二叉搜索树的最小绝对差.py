# https://leetcode.cn/problems/minimum-absolute-difference-in-bst

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self._min = float('inf')

        def traverse(root):
            if root is None:
                return
            
            traverse(root.left)
            
            if self.prev is None:
                pass
            else:
                diff = root.val - self.prev.val
                self._min = min(self._min, diff)

            self.prev = root

            traverse(root.right)

        traverse(root)
        return self._min