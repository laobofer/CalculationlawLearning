# https://leetcode.cn/problems/add-one-row-to-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        from collections import deque

        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node

        q = deque()
        q.append(root)
        cur_depth = 0

        while q:
            size = len(q)
            cur_depth += 1

            if cur_depth > depth:
                break

            for _ in range(size):
                node = q.popleft()
                old_left, old_right = node.left, node.right
                if cur_depth == depth - 1:
                    new_left, new_right = TreeNode(val), TreeNode(val)
                    node.left, node.right = new_left, new_right
                    new_left.left, new_right.right = old_left, old_right

                if old_left is not None:
                    q.append(old_left)
                if old_right is not None:
                    q.append(old_right)

        return root

        
