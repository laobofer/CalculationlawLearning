# https://leetcode.cn/problems/maximum-width-of-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        from collections import deque
        q = deque()
        q.append([root, 1])
        res = 0

        while q:
            size = len(q)
            index1, index2 = 0, 0

            for i in range(size):
                node, index = q.popleft()
                if i == 0:
                    index1 = index
                if size - i - 1 == 0:
                    index2 = index
                
                if node.left:
                    q.append([node.left, index * 2])
                if node.right:
                    q.append([node.right, index * 2 + 1])

            res = max(index2 - index1 + 1, res)

        return res
