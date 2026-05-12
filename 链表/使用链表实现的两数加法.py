# https://leetcode.cn/problems/add-two-numbers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_val(self, head):
        return head.val if head else 0

    def next_node(self, head):
        return head.next if head is not None and head.next else None

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        ret = ListNode(-1)
        p = ret

        sum_next = 0
        while True:
            sum = self.get_val(p1) + self.get_val(p2) + sum_next
            sum_here = sum % 10
            sum_next = sum // 10
            p.next = ListNode(sum_here)
            p = p.next
            p1, p2 = self.next_node(p1), self.next_node(p2)

            if not p1 and not p2 and sum_next == 0:
                break

        return ret.next

        