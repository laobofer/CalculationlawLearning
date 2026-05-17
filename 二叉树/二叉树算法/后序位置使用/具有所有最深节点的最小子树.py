# https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            """返回: 以 root 为根子树的最大深度, 具有所有最深节点子树的根节点"""

            if root is None:
                return 0, None
            
            l_depth, l_node = helper(root.left)
            r_depth, r_node = helper(root.right)
            
            res = None
            if l_depth == r_depth:
                res = root
            elif l_depth > r_depth:
                res = l_node
            else:
                res = r_node

            return max(l_depth, r_depth) + 1, res
        
        _, res = helper(root)
        return res