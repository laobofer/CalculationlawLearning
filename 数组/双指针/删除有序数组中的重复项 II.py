# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        cur_num = 10001
        num = 1
        ret = 0

        while fast < len(nums):
            if cur_num != nums[fast]:
                cur_num = nums[fast]
                nums[slow] = cur_num
                slow += 1
                num = 1
                ret += 1
            else:                
                if num == 1:
                    nums[slow] = cur_num
                    slow += 1
                    num = 1
                    ret += 1
                num += 1

            fast += 1

        return ret

            