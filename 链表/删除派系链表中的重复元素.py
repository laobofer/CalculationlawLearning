# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyUniq = ListNode(101)
        dummyDup = ListNode(101)

        pUniq, pDup = dummyUniq, dummyDup
        p = head

        while p is not None:
            if (p.next is not None and p.val == p.next.val) or p.val == pDup.val:
                pDup.next = p
                pDup = pDup.next
            else:
                pUniq.next = p
                pUniq = pUniq.next

            p = p.next
            pUniq.next = None
            pDup.next = None

        return dummyUniq.next



