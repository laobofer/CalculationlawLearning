# https://leetcode.cn/problems/maximum-binary-tree-ii

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_lst_a(self, root):
        if root is None:
            return []

        left = self.get_lst_a(root.left)
        right = self.get_lst_a(root.right)
        return left + [root.val] + right

    def makeMaxTree(self, lst, lo, hi):
        if not lst or lo >= hi:
            return None

        root_val = max(lst[lo:hi])
        index = lst[lo:hi].index(root_val) + lo

        left = self.makeMaxTree(lst, lo, index)
        right = self.makeMaxTree(lst, index + 1, hi)

        root = TreeNode(root_val, left, right)

        return root

    def insertIntoMaxTree(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        a = self.get_lst_a(root)
        b = a + [val]

        return self.makeMaxTree(b, 0, len(b))



class Solution2:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if root.val < val:
            temp = root
            root = TreeNode(val)
            root.left = temp
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
        return root