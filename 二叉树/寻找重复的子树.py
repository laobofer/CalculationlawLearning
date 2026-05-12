# https://leetcode.cn/problems/find-duplicate-subtrees

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        from collections import defaultdict
        nodes = defaultdict(int)
        res = []
        def helper(root):
            """记录 nodes 的信息: 从每个节点为根的子树的结构, 返回每个节点先序遍历的结果"""
            if root is None:
                return "#"
            
            left = helper(root.left)
            right = helper(root.right)

            s = ','.join([str(root.val), left, right])

            nodes[s] += 1
            if nodes[s] == 2:
                res.append(root)

            return s
        
        helper(root)
        return res
