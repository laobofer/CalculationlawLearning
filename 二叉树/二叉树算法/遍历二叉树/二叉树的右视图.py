# https://leetcode.cn/problems/binary-tree-right-side-view

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 也可以用层序遍历实现

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)

        res.append(root.val)
        if len(left) <= len(right):
            res.extend(right)
        else:
            res.extend(right)
            res.extend(left[len(right):])

        return res