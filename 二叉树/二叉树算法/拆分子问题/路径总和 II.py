# https://leetcode.cn/problems/path-sum-ii

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def traverse(self, root, targetSum):
        if root is None:
            return
        
        self.path.append(root.val)

        if root.left is None and root.right is None:
            if sum(self.path) == targetSum:
                self.res.append(self.path.copy())

        self.traverse(root.left, targetSum)
        self.traverse(root.right, targetSum)

        self.path.pop()


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.traverse(root, targetSum)
        return self.res 