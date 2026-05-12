# https://leetcode.cn/problems/minimum-window-substring

class Solution:
    def is_right_substr(self, mine, need):
        for chr, num in need.items():
            if mine[chr] < num:
                return False
            
        return True
    
    

    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        window = defaultdict(int)
        need = defaultdict(int)

        for chr in t:
            need[chr] += 1

        left, right = 0, 0
        res = [0, 0]

        while right < len(s):
            chr = s[right]
            window[chr] += 1
            right += 1        

            while left < right and self.is_right_substr(window, need):
                new_answer = [left, right]
                res[:] = new_answer if (right - left) < (res[1] - res[0]) or res == [0, 0] else res

                chr = s[left]
                left += 1
                window[chr] -= 1


        return s[res[0]:res[1]]



