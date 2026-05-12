# https://leetcode.cn/problems/reverse-linked-list-ii

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        
        pre = head
        for _ in range(left-2):
            pre = pre.next
        
        pre.next = self.reverseN(pre.next, right - left + 1)
        return head
    
    def reverseN(self, head, n):
        if head is None or head.next is None:
            return head

        pre, cur, nxt = None, head, head.next

        for _ in range(n):
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt is not None:
                nxt = nxt.next

        head.next = cur
        
        return pre
        
        
s = Solution()
s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)

