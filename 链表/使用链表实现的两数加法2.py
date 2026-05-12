# https://leetcode.cn/problems/add-two-numbers-ii

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 把链表元素转入栈中
        stk1 = []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        stk2 = []
        while l2:
            stk2.append(l2.val)
            l2 = l2.next

        dummy = ListNode(-1)

        carry = 0
        while stk1 or stk2 or carry > 0:
            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()

            carry = val // 10
            val = val % 10

            newNode = ListNode(val)
            newNode.next = dummy.next
            dummy.next = newNode

        return dummy.next
        

        