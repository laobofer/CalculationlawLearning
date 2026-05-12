# https://leetcode.cn/problems/partition-list
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res_left = ListNode(-101)
        res_right = ListNode(-101)

        p = head
        p1 = res_left
        p2 = res_right

        while p is not None:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            
            temp = p.next
            p.next = None
            p = temp

        p1.next = res_right.next

        return res_left.next

            

            
