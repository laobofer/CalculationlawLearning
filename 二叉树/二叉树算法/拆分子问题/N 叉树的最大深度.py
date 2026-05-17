# https://leetcode.cn/problems/maximum-depth-of-n-ary-tree

from typing import Optional, List

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.res = -float("inf")

    def traverse(self, root, depth):
        if root is None:
            return

        if all(child is None for child in root.children):
            self.res = max(self.res, depth)

        for child in root.children:
            self.traverse(child, depth + 1)

    def maxDepth(self, root: "Node") -> int:
        self.traverse(root, 1)
        return self.res if root else 0