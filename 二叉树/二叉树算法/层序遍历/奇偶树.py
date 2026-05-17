# https://leetcode.cn/problems/even-odd-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def check(lst, isEven):
            if isEven:
                if lst[-1] % 2 != 1:
                    return False
                for i in range(len(lst) - 1):
                    if lst[i] % 2 != 1:
                        return False
                    if lst[i] >= lst[i + 1]:
                        return False
                    
                return True
            else:
                if lst[-1] % 2 != 0:
                    return False
                for i in range(len(lst) - 1):
                    if lst[i] % 2 != 0:
                        return False
                    if lst[i] <= lst[i + 1]:
                        return False
                    
                return True                
                    
        
        from collections import deque
        q = deque()
        q.append(root)
        isEven = False

        while q:
            size = len(q)
            isEven = not isEven
            lst = []

            for _ in range(size):
                node = q.popleft()
                lst.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if not check(lst, isEven):
                return False
            
        return True