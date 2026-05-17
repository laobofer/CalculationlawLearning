# https://leetcode.cn/problems/check-completeness-of-a-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        from collections import deque

        q = deque()
        q.append([root, 1])
        depth = 0

        while q:
            size = len(q)
            depth += 1
            index1, index2 = 0, 0

            for i in range(size):
                node, index = q.popleft()

                if i == 0:
                    index1 = index
                if i == size - 1:
                    index2 = index

                if node.left:
                    q.append([node.left, index * 2])
                if node.right:
                    q.append([node.right, index * 2 + 1])

            if size != 2 ** (depth - 1) and q:
                return False

            if not q and index2 - index1 + 1 != size:
                return False

            if index1 != 2 ** (depth - 1):
                return False

        return True