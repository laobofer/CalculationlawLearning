# https://leetcode.cn/problems/reorder-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pp = head
        p = head
        stack = []

        len_ = 0
        while pp:
            stack.append(pp)
            pp = pp.next
            len_ += 1

        for _ in range(len_ // 2):
            temp = p.next
            p.next = stack.pop()
            p.next.next = temp
            p = p.next.next

        p.next = None

Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))



        

        
