# https://leetcode.cn/problems/find-the-duplicate-number

from typing import List

# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

# 这里的取值都在 [1, n] 之间, 可以联想到链表 ListNode(0) -> ListNode(nums[0]) -> ListNode(nums[nums[0]])

class Solution:
    def next_node(self, nums, next):
        return nums[next]
    
    def next_next_node(self, nums, next):
        return nums[nums[next]]


    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = self.next_next_node(nums, fast)
            slow = self.next_node(nums, slow)
            if slow == fast:
                break

        slow = 0

        while fast != slow:
            slow = self.next_node(nums, slow)
            fast = self.next_node(nums, fast)

        return slow

