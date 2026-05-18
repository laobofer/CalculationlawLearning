# https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        lst = []
        p = head
        while p:
            lst.append(p.val)
            p = p.next

        def helper(lo, hi):
            if lo >= hi:
                return None
            
            index = (hi - lo) // 2 + lo
            root_val = lst[index]

            left = helper(lo, index)
            right = helper(index + 1, hi)

            return TreeNode(root_val, left, right)
        
        return helper(0, len(lst))
    

# 可以用中序遍历的特性优化
class Solution2:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def inorderBuild(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right) // 2
            leftTree = inorderBuild(left, mid - 1)
            root = TreeNode(self.cur.val)
            self.cur = self.cur.next
            rightTree = inorderBuild(mid + 1, right)
            root.left = leftTree
            root.right = rightTree
            return root

        len = 0
        p = head
        while p:
            len += 1
            p = p.next

        self.cur = head
        return inorderBuild(0, len - 1)