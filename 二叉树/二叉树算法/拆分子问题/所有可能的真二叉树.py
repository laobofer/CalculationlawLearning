# https://leetcode.cn/problems/all-possible-full-binary-trees

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    from functools import lru_cache

    @lru_cache
    def make_trees(self, n):
        if n == 0:
            return [None]

        res = []

        for i in range(n):
            lefts = self.make_trees(i)
            rights = self.make_trees(n - i - 1)

            for left in lefts:
                for right in rights:
                    root = TreeNode(0, left, right)
                    if (left and right) or (not left and not right):
                        res.append(root)

        return res

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        trees = self.make_trees(n)
        return trees

