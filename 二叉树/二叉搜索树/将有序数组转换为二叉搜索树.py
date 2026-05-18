# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(lo, hi):
            if lo >= hi:
                return None
            
            _len = hi - lo
            index = _len // 2 + lo
            root_val = nums[index]

            left = helper(lo, index)
            right = helper(index + 1, hi)

            root = TreeNode(root_val, left, right)

            return root
        
        return helper(0, len(nums))
