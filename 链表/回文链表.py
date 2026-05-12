# https://leetcode.cn/problems/palindrome-linked-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        p1 = head
        p2 = head


        while p1:
            stack.append(p1.val)
            p1 = p1.next

        while stack and p2:
            val = stack.pop()
            if val != p2.val:
                return False
            
            p2 = p2.next
            
        return True

