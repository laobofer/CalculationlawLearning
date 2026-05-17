# https://leetcode.cn/problems/binary-tree-cameras

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(root, has_parent):
            """
            返回某节点的状态
            -1 -> 空节点 0 -> 尚未被覆盖节点 1 -> 被覆盖节点 2 -> 摄像头
            """
            if root is None:
                return -1 
            
            left = helper(root.left, True)
            right = helper(root.right, True)

            if left == -1 and right == -1:
                if has_parent:
                    return 0
                self.res += 1
                return 2
            
            if left == 0 or right == 0:
                self.res += 1
                return 2
            
            if left == 2 or right == 2:
                return 1
            
            if has_parent:
                return 0
            else:
                self.res += 1
                return 2
            
        helper(root, False)
        return self.res