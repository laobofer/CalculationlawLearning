# https://leetcode.cn/problems/maximum-binary-tree

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums, lo, hi):
            """返回这一段的树的根, 左闭右开"""
            if lo >= hi:
                return None

            val = max(nums[lo: hi])
            index = nums[lo: hi].index(val) + lo

            left = helper(nums, lo, index)
            right = helper(nums, index + 1, hi)

            root = TreeNode(val, left, right)

            return root

        return helper(nums, 0, len(nums))
    
print(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))