# https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_product = -float('inf')
        self.all_sum = 0

    def traverse(self, root):
        if root is None:
            return
        
        self.all_sum += root.val

        self.traverse(root.left)
        self.traverse(root.right)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)

        def helper(root):
            """返回以此为根的子树的和"""
            if root is None:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            self.max_product = max(self.max_product, left * (self.all_sum - left), right * (self.all_sum - right))

            return left + right + root.val
        
        helper(root)

        return self.max_product % (10**9 + 7)
