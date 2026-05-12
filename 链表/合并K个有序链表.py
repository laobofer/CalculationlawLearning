# https://leetcode.cn/problems/merge-k-sorted-lists

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        if not lists:
            return None
        
        pq = []
        res = ListNode(-101)
        p = res

        for index, list in enumerate(lists):
            if list is not None:
                heapq.heappush(pq, (list.val, index, list))

        while not pq:
            _, index, head = heapq.heappop()
            p.next = head

            head = head.next
            if head:
                heapq.heappush(pq, (head.val, index, head))

            p = p.next

        return res.next


