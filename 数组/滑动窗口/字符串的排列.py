# https://leetcode.cn/problems/permutation-in-string

class Solution:
    def is_right_substr(self, mine, need):
        if len(mine) != len(need):
            return False

        for chr, num in need.items():
            if mine[chr] != need[chr]:
                return False

        return True
    
    def need_shrink(self, left, right, length):
        return right - left == length

    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict

        window = defaultdict(int)
        need = defaultdict(int)

        for chr in s1:
            need[chr] += 1

        left, right = 0, 0

        while right < len(s2):
            chr = s2[right]
            window[chr] += 1
            right += 1
        
            while left < right and self.need_shrink(left, right, len(s1)):
                if self.is_right_substr(window, need):
                    return True

                chr = s2[left]
                window[chr] -= 1
                if window[chr] == 0:
                    del window[chr]
                left += 1

        return False


print(Solution().checkInclusion("ab", "eidbaooo"))