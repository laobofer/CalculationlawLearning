# https://leetcode.cn/problems/4sum

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            pairs = self.threeSumTarget(nums, i + 1, target - nums[i])

            for pair in pairs:
                pair.append(nums[i])
                res.append(pair)

            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    i += 1
                else:
                    break

            i += 1

        return res        
        
    def threeSumTarget(self, nums: List[int], start, target: int) -> List[List[int]]:
        # nums.sort()
        res = []

        i = start
        while i < len(nums):
            pairs = self.twoSumTarget(nums, i + 1, target - nums[i])

            for pair in pairs:
                pair.append(nums[i])
                res.append(pair)

            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    i += 1
                else:
                    break

            i += 1
        
        return res



    def twoSumTarget(self, nums, start, target):
        lo, hi = start, len(nums) - 1
        res = []

        while lo < hi:
            sum = nums[lo] + nums[hi]

            if sum > target:
                hi -= 1
            elif sum < target:
                lo += 1
            else:
                res.append([nums[lo], nums[hi]])

                for i in range(lo + 1, hi):
                    if nums[i] == nums[lo]:
                        lo += 1
                    else:
                        break
                
                for i in range(hi - 1, lo, -1):
                    if nums[i] == nums[hi]:
                        hi -= 1
                    else:
                        break

                lo += 1
                hi -= 1                    

        return res
