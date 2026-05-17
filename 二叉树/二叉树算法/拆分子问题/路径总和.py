# https://leetcode.cn/problems/path-sum

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum = 0
        self.res = False

    def traverse(self, root, targetSum):
        if self.res:
            return

        if root is None:
            return
        
        self.sum += root.val

        if root.left is None and root.right is None:
            if self.sum == targetSum:
                self.res = True

        self.traverse(root.left, targetSum)
        self.traverse(root.right, targetSum)

        self.sum -= root.val


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.traverse(root, targetSum)

        return self.res 