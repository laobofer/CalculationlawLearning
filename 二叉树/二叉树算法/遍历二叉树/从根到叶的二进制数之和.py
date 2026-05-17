# https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.cur_num = ''
        self.sum = 0

    def traverse(self, root):
        if root is None:
            return
        
        self.cur_num += str(root.val)

        if root.left is None and root.right is None:
            num = int(self.cur_num, 2)
            self.sum += num

        self.traverse(root.left)
        self.traverse(root.right)

        self.cur_num = self.cur_num[0: -1]

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)

        return self.sum