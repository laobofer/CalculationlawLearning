# https://leetcode.cn/problems/binary-search-tree-iterator

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        from collections import deque
        self.lst = deque()

        def helper(root):
            if root is None:
                return
            
            helper(root.left)
            self.lst.append(root.val)
            helper(root.right)
        helper(root)

    def next(self) -> int:
        val = self.lst.popleft()
        return val

    def hasNext(self) -> bool:
        return len(self.lst) >= 1