# https://leetcode.cn/problems/count-good-nodes-in-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 可以通过把最大值作为参数来优化
class Solution:
    def __init__(self):
        self.path = []
        self.count = 0

    def traverse(self, root):
        if root is None:
            return
        self.path.append(root.val)

        if root.val >= max(self.path):
            self.count += 1

        self.traverse(root.left)
        self.traverse(root.right)

        self.path.pop()

    def goodNodes(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)

        return self.count


