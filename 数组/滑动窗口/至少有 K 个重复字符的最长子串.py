# https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters

# 此题不可直接滑动窗口, 因为扩张和收缩的逻辑不能直接确定
# 分治 或 调整后滑动窗口

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return max([self.longestSubstring_with_n_chrs(s, k, i)for i in range(1, 26 + 1)])

    def need_shrink(self, count, n):
        return count > n

    def longestSubstring_with_n_chrs(self, s: str, k: int, n):
        from collections import defaultdict
        window = defaultdict(int)

        left, right = 0, 0
        res = 0
        while right < len(s):
            chr = s[right]
            window[chr] += 1
            right += 1

            while left < right and self.need_shrink(len(window), n):
                chr = s[left]
                window[chr] -= 1
                if window[chr] == 0:
                    del window[chr]
                left += 1

            if all([1 if num >= k else 0 for chr, num in window.items()]):
                res = max(res, right - left)

        return res

            







# 分治法
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         if min([s.count(chr) for chr in s]) >= k:
#             return len(s)
        
#         if all([1 if s.count(chr) < k else 0 for chr in s]):
#             return 0

#         strs = [[]]
#         i = 0
#         for chr in s:
#             if s.count(chr) < k:
#                 i += 1
#                 strs.append([])
#             else:
#                 strs[i].append(chr)

#         while [] in strs:
#             strs.remove([])

#         return max([self.longestSubstring(str, k) for str in strs])



print(Solution().longestSubstring("aaabb", 3))