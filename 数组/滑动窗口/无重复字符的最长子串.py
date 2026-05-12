# https://leetcode.cn/problems/longest-substring-without-repeating-characters

class Solution:
    def need_shrink(self, window, chr):
        return window[chr] >= 2
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        window = defaultdict(int)

        left, right = 0, 0
        res = 0

        while right < len(s):
            chr = s[right]
            window[chr] += 1
            right += 1

            if window[chr] == 1:
                res = max(right - left, res)

            while left < right and self.need_shrink(window, chr):
                chr_ = s[left]
                window[chr_] -= 1
                left += 1

        return res

Solution().lengthOfLongestSubstring("pwwkew")