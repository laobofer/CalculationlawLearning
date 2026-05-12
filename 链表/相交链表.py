# https://leetcode.cn/problems/intersection-of-two-linked-lists

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set_a = set()
        p = headA
        while p:
            set_a.add(p)
            p = p.next

        p = headB
        while p:
            if p in set_a:
                return p
            p = p.next

        return None
            
        