# https://leetcode.cn/problems/convert-bst-to-greater-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_right_sum(self, root):
        # 返回某节点下所有元素之和
        if root is None:
            return 0
        
        left = self.get_right_sum(root.left)
        right = self.get_right_sum(root.right)

        root.r_sum = right

        return root.r_sum + left + root.val
    
    def traverse(self, root, parent_val):
        if root is None:
            return
        
        root.val = parent_val + root.r_sum + root.val
        self.traverse(root.left, root.val)
        self.traverse(root.right, parent_val)


    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.get_right_sum(root)
        self.traverse(root, 0)

        return root
    
# 此题也可利用 二叉搜索树 中序遍历有序的特性, 直接找到某节点的该有的值

class Solution2:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if root is None:
                return
            
            traverse(root.right)

            self.sum += root.val
            root.val = self.sum

            traverse(root.left)

        traverse(root)

        return root