# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "#"

        left = self.serialize(root.left)
        right = self.serialize(root.right)

        s = ",".join([str(root.val), left, right])
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")

        def helper(data):
            root_val = data.pop(0)

            if root_val == "#":
                return None

            left = helper(data)
            right = helper(data)
            root = TreeNode(int(root_val), left, right)

            return root

        return helper(data)