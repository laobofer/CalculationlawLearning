# https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pathSum = 0

    def traverse(self, root):
        if root is None:
            return

        self.pathSum += root.val

        root.sum2here = self.pathSum

        self.traverse(root.left)
        self.traverse(root.right)

        self.pathSum -= root.val

    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        self.traverse(root)

        def helper(root):
            """返回: 从此节点到第一个叶子节点的最大的路径和"""
            if root is None:
                return -float('inf')
            
            if root.left is None and root.right is None:
                return root.val

            left = helper(root.left)
            right = helper(root.right)

            if root.left and left - root.left.val + root.left.sum2here < limit:
                root.left = None
            if root.right and right - root.right.val + root.right.sum2here < limit:
                root.right = None

            return root.val + max(left, right)
        

        if helper(root) < limit:
            root = None

        return root


# 可以优化为两个一起计算
class Solution2:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        def helper(node, parent_sum):
            """返回: 从此节点到第一个叶子节点的最大的路径和"""
            if not node:
                return float("-inf")

            current_sum = parent_sum + node.val

            if not node.left and not node.right:
                return node.val

            left_max = helper(node.left, current_sum)
            right_max = helper(node.right, current_sum)

            if node.left and current_sum + left_max < limit:
                node.left = None
            if node.right and current_sum + right_max < limit:
                node.right = None

            return node.val + max(left_max, right_max)

        root_max = helper(root, 0)

        return root if root_max >= limit else None