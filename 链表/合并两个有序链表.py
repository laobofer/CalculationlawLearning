# https://leetcode.cn/problems/merge-two-sorted-lists/description/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1000)
        p = res
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                p.next = list1
                p = p.next
                list1 = list1.next
            else:
                p.next = list2
                p = p.next
                list2 = list2.next

        if list1 is not None:
            p.next = list1

        if list2 is not None:
            p.next = list2

        return res.next
