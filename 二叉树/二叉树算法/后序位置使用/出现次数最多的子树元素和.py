# https://leetcode.cn/problems/most-frequent-subtree-sum

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        from collections import defaultdict

        self.dict = defaultdict(int)

    def get_num(self, root):
        """返回以此为根的子树的节点的和"""
        if root is None:
            return 0

        left = self.get_num(root.left)
        right = self.get_num(root.right)

        self.dict[root.val + left + right] += 1
        return root.val + left + right

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.get_num(root)
        res = []

        _max = max(self.dict.values())

        for key, value in self.dict.items():
            if value == _max:
                res.append(key)

        return res
