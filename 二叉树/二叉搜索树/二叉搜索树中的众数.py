# https://leetcode.cn/problems/find-mode-in-binary-search-tree

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict

        self.dict = defaultdict(int)

        def traverse(root):
            if root is None:
                return

            self.dict[root.val] += 1

            traverse(root.left)
            traverse(root.right)

        traverse(root)
        max_num = max(self.dict.values())
        res = [key for key, val in self.dict.items() if max_num == val]
        return res


