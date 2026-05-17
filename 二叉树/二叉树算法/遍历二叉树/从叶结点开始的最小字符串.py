# https://leetcode.cn/problems/smallest-string-starting-from-leaf

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.min_str = ''
        self.cur_str = ''

    def traverse(self, root):
        if root is None:
            return
        
        self.cur_str = chr(root.val + ord("a")) + self.cur_str

        if root.left is None and root.right is None:
            self.min_str = (
                min(self.min_str, self.cur_str) if self.min_str else self.cur_str
            )

        self.traverse(root.left)
        self.traverse(root.right)

        self.cur_str = self.cur_str[1:]


    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.traverse(root)

        return self.min_str