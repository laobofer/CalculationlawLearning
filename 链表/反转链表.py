# https://leetcode.cn/problems/reverse-linked-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代实现
        if head is None or (head is not None and head.next is None):
            return head
        
        pre, cur, nxt = None, head, head.next

        while cur:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt is not None:
                nxt = nxt.next

        return pre
    
    def reverseList_(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or (head is not None and head.next is None):
            return head
        
        new_link_last = head.next
        
        new_head = self.reverseList_(head.next)

        new_link_last.next = head
        head.next = None

        return new_head
        