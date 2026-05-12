# https://leetcode.cn/problems/find-k-closest-elements

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import bisect
        p = bisect.bisect_left(arr, x)

        left = p - 1
        right = p

        remain = k
        res = []

        while left >= 0 and right < len(arr):
            if remain == 0:
                break

            if abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
                remain -= 1
            else:
                res.append(arr[right])
                remain -= 1
                right += 1

        while left >= 0:
            if remain == 0:
                break
            res.append(arr[left])
            left -= 1
            remain -= 1

        while right < len(arr):
            if remain == 0:
                break
            res.append(arr[right])
            remain -= 1
            right += 1         
        
        res.sort()
        return res


print(Solution().findClosestElements([1, 2, 4, 5], 4, 3))

