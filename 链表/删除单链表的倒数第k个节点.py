# https://leetcode.cn/problems/remove-nth-node-from-end-of-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_ = ListNode(-1)
        list_.next = head
        node = self.getNthFromEnd(list_, n+1)
        node.next = node.next.next
        return list_.next


    
    def getNthFromEnd(self, head: Optional[ListNode], n: int):
        fast, slow = head, head

        for _ in range(n - 1):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        return slow        
