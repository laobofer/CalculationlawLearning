# https://leetcode.cn/problems/longest-repeating-character-replacement

class Solution:
    def need_shrink(self, window, k):
        most_chr, num = max([(chr, num) for chr, num in window.items()], key=lambda x: x[1])
        all_chr_num = sum([num for chr, num in window.items()])
        return all_chr_num - num > k

    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        window = defaultdict(int)

        left, right = 0, 0
        res = 0

        while right < len(s):
            chr = s[right]
            window[chr] += 1
            right += 1

            while left < right and self.need_shrink(window, k):
                chr = s[left]
                window[chr] -= 1
                left += 1

            res = max(right - left, res)

        return res