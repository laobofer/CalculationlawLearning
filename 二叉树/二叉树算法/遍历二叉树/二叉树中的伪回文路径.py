# https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        from collections import defaultdict

        self.dict = defaultdict(int)
        self.res = 0
        self.cur_path = []

    def _isValid(self, dict):
        odd_num = 0
        for key, value in dict.items():
            if value % 2 == 1:
                odd_num += 1
                if odd_num >= 2:
                    return False

        return True

    def traverse(self, root):
        if root is None:
            return

        self.cur_path.append(root.val)
        self.dict[root.val] += 1

        if root.left is None and root.right is None:
            if self._isValid(self.dict):
                self.res += 1

        self.traverse(root.left)
        self.traverse(root.right)

        self.cur_path.pop()
        self.dict[root.val] -= 1

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)

        return self.res