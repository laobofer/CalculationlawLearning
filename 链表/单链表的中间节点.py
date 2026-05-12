# https://leetcode.cn/problems/middle-of-the-linked-list

from typing import Optional

# 检测边界 !!!!


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow if fast.next is None else slow.next

        