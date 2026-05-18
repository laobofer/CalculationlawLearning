# https://leetcode.cn/problems/all-elements-in-two-binary-search-trees

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 可以用 生成器 + 迭代器 来减少内存占用

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def getList(root):
            if root is None:
                return []
            
            left = getList(root.left)
            right = getList(root.right)
            return left + [root.val] + right
        
        lst1 = getList(root1)
        lst2 = getList(root2)

        i, j = 0, 0
        res = []

        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                j += 1

        while i < len(lst1):
            res.append(lst1[i])
            i += 1

        while j < len(lst2):
            res.append(lst2[j])
            j += 1

        return res
