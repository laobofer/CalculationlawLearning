# https://leetcode.cn/problems/rotate-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_end(self, head):
        p = head
        len_ = 1
        while p.next:
            p = p.next
            len_ += 1

        return p, len_


    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        ret = head
        p, len_ = self.get_end(head)
        p.next = head

        k = k % len_
        
        ret_pre = head
        for i in range(len_ - k):
            if i != 0:
                ret_pre = ret_pre.next
            ret = ret.next

        ret_pre.next = None

        return ret
