# https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def traverse(root, parent):
            if root is None:
                return

            root.father = parent

            traverse(root.left, root)
            traverse(root.right, root)

        traverse(root, None)

        from collections import deque

        q = deque()
        q.append(target)
        width = -1
        _set = set()
        _set.add(target.val)
        res = []

        while q:
            size = len(q)
            width += 1

            if width > k:
                break

            for _ in range(size):
                node = q.popleft()
                if width == k:
                    res.append(node.val)

                if node.left and node.left.val not in _set:
                    _set.add(node.left.val)
                    q.append(node.left)
                if node.right and node.right.val not in _set:
                    _set.add(node.right.val)
                    q.append(node.right)
                if node.father and node.father.val not in _set:
                    _set.add(node.father.val)
                    q.append(node.father)

        return res