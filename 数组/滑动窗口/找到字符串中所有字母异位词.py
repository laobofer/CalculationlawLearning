# https://leetcode.cn/problems/find-all-anagrams-in-a-string

from typing import List

class Solution:
    def need_shrink(self, left, right, length):
        return right - left == length

    def is_right_substr(self, mine, need):
        if len(need) != len(mine):
            return False
        
        for chr, num in need.items():
            if mine[chr] != need[chr]:
                return False
            
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict
        window = defaultdict(int)
        need = defaultdict(int)

        for chr in p:
            need[chr] += 1

        left, right = 0, 0
        res = []

        while right < len(s):
            chr = s[right]
            window[chr] += 1
            right += 1

            while left < right and self.need_shrink(left, right, len(p)):
                if self.is_right_substr(window, need):
                    res.append(left)

                chr = s[left]
                window[chr] -= 1
                if window[chr] == 0:
                    del window[chr]
                left += 1

        return res

print(Solution().findAnagrams("abab", "ab"))