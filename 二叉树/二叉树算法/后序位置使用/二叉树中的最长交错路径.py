# https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_len = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            """
            返回: root 第一步向左的最长路径上的节点数, root 第一步向右的最长路径上的节点数
            """
            if root is None:
                return 0, 0
            
            l_l, l_r = helper(root.left)
            r_l, r_r = helper(root.right)

            cur_l = 1 + l_r
            cur_r = 1 + r_l

            self.max_len = max(self.max_len, cur_l, cur_r)

            return cur_l, cur_r
        
        helper(root)
        return self.max_len - 1


