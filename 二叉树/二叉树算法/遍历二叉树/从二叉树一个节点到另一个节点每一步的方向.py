# https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.path = []
        self.path2start = []
        self.path2dest = []

    def traverse(self, root, startValue, destValue):
        if root is None:
            return

        self.path.append(root)

        if root.val == startValue:
            self.path2start = self.path.copy()
            self.path2start.reverse()

        if root.val == destValue:
            self.path2dest = self.path.copy()
            self.path2dest.reverse()

        self.traverse(root.left, startValue, destValue)
        self.traverse(root.right, startValue, destValue)

        self.path.pop()

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        self.traverse(root, startValue, destValue)
        dict = {}
        for node in self.path2start:
            dict[node.val] = 1

        dict2 = {}

        for node in self.path2dest:
            dict2[node.val] = 1

        first_node = None

        for node in self.path2dest:
            if node.val in dict:
                first_node = node
                break

        num1 = self.path2start.index(first_node)
        res = "U" * num1

        while True:
            if first_node is self.path2dest[0]:
                break
            if first_node.left and first_node.left.val in dict2:
                res += "L"
                first_node = first_node.left
            if first_node.right and first_node.right.val in dict2:
                res += "R"
                first_node = first_node.right

        return res