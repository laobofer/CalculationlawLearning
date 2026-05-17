# https://leetcode.cn/problems/binary-tree-coloring-game

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.node_x = None
        self.node_x_f = None
        self.node_x_l = None
        self.node_x_r = None

    def get_num_of_nodes(self, root):
        if root is None:
            return 0
        
        left = self.get_num_of_nodes(root.left)
        right = self.get_num_of_nodes(root.right)

        root.num = left + right + 1

        return root.num
    
    def traverse(self, root, x):
        if root is None:
            return
        
        if root.left and root.left.val == x:
            self.node_x_f = root
        if root.right and root.right.val == x:
            self.node_x_f = root

        if root.val == x:
            self.node_x = root
            self.node_x_l = root.left
            self.node_x_r = root.right

        self.traverse(self, root, x)
        self.traverse(self, root, x)


    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.get_num_of_nodes(root)
        self.traverse(root, x)

        num1 = self.node_x_l.num if self.node_x_l else 0
        num2 = self.node_x_r.num if self.node_x_r else 0

        num3 = (
            self.node_x_f.num - self.node_x.num
            if self.node_x_f
            else max(num1, num2)
        )

        num3 = max(num3, n - self.node_x.num)

        return max(num1, num2, num3) > n / 2
    
# 一种优化的写法

class Solution2:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        node = self.find(root, x)
        left_count = self.count(node.left)
        right_count = self.count(node.right)
        other_count = n - 1 - left_count - right_count

        return max(left_count, right_count, other_count) > n / 2

    # 定义：在以 root 为根的二叉树中搜索值为 x 的节点并返回
    def find(self, root: TreeNode, x: int) -> TreeNode:
        if root is None:
            return None
        if root.val == x:
            return root
        left = self.find(root.left, x)
        if left is not None:
            return left
        return self.find(root.right, x)

    def count(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
