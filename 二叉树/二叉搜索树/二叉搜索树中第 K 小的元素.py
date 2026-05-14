# https://leetcode.cn/problems/kth-smallest-element-in-a-bst

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.lst = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.finded = False

        def traverse(root):
            if root is None or self.finded:
                return
            
            traverse(root.left)

            self.lst.append(root.val)
            if len(self.lst) == k:
                self.finded = True

            traverse(root.right)

        traverse(root)

        return self.lst[k - 1]

        

        