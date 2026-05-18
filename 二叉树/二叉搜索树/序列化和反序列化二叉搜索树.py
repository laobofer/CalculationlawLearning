# https://leetcode.cn/problems/serialize-and-deserialize-bst

from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""

        def helper(root):
            if root is None:
                return "#"

            left = helper(root.left)
            right = helper(root.right)

            return str(root.val) + "," + left + "," + right

        return helper(root)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        data = data.split(",")

        def helper(data):
            data_val = data.pop(0)

            if data_val == "#":
                return None

            left = helper(data)
            right = helper(data)

            return TreeNode(int(data_val), left, right)

        return helper(data)
