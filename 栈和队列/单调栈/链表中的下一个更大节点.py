# https://leetcode.cn/problems/next-greater-node-in-linked-list

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        lst = []
        p = head

        while p:
            lst.append(p.val)
            p = p.next

        n = len(lst)
        res = [0 for _ in range(n)]
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= lst[i]:
                stack.pop()

            res[i] = 0 if not stack else stack[-1]
            stack.append(lst[i])

        return res